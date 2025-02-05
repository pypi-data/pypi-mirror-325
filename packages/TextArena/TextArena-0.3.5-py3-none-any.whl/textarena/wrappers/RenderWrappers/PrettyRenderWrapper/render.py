from typing import Dict, Optional, Any
import time
from playwright.sync_api import sync_playwright
import cv2
import numpy as np
from PIL import Image
import io
import os

try:
    from pyngrok import ngrok
    NGROK_AVAILABLE = True
except ImportError:
    NGROK_AVAILABLE = False

class PrettyRenderWrapper:
    def __init__(
        self,
        env: Any,
        player_names: Optional[Dict[int, str]] = None,
        port: int = 8000,
        host: str = "127.0.0.1",
        use_ngrok: bool = False,
        allow_local_network: bool = True,  # New parameter
        record_video: bool = False, 
        video_path: str = "game_recording.mp4"
    ):
        self.env = env
        self.port = port
        self.host = "0.0.0.0" if allow_local_network else host  # Use 0.0.0.0 for local network access
        self.chat_history = []
        self.record_video = record_video
        self.video_path = video_path
        
        if not hasattr(self.env, 'offline_renderer'):
            raise AttributeError("Environment must have 'offline_renderer' attribute")
        
        # Initialize renderer
        self.renderer = self.env.offline_renderer(
            env=self.env, 
            player_names=player_names, 
            port=port,
            host=self.host
        )
        
        # Setup frames list if recording video
        if self.record_video:
            self.frames = []

        # Set up URL
        if use_ngrok:
            self._setup_ngrok()
        else:
            self.url = f"http://127.0.0.1:{port}"  # Always use localhost for the URL

        # Print access information
        self._print_access_info()

    def _setup_ngrok(self):
        """Set up ngrok tunnel if available"""
        if not NGROK_AVAILABLE:
            print("Ngrok support requested but pyngrok is not installed. Install with: pip install pyngrok")
            self.url = f"http://{self.host}:{self.port}"
            return

        try:
            public_url = ngrok.connect(self.port).public_url
            self.url = public_url
            print("\nNgrok tunnel established!")
        except Exception as e:
            print(f"Failed to establish ngrok tunnel: {e}")
            self.url = f"http://{self.host}:{self.port}"

    def _print_access_info(self):
        """Print access information to console"""
        print(f"\nTextArena server running at: {self.url}")
        
        try:
            import socket
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            local_ip = s.getsockname()[0]
            s.close()
            if self.host == "0.0.0.0":
                print(f"Local network access: http://{local_ip}:{self.port}")
        except Exception as e:
            print(f"Could not determine local network address: {e}")

        print("\nPress Ctrl+C to stop the server")

    def _capture_frame_with_playwright(self):
        with sync_playwright() as p:
            # Launch browser
            self.browser = p.chromium.launch(
                headless=True,
                args=["--disable-web-security", "--start-maximized"]
            )
            
            # Open a new page in the browser
            context = self.browser.new_context(
                viewport={"width": 1920, "height": 2160},  # Default size
            )
            page = context.new_page()
            page.goto(self.url)
            
            # Wait for the page to load
            time.sleep(0.5)
            
            # Generalize scrolling for all scrollable elements
            try:
                page.evaluate("""
                    // Get all scrollable elements on the page
                    const scrollableElements = Array.from(document.querySelectorAll('*')).filter(el => {
                        const style = getComputedStyle(el);
                        return (
                            el.scrollHeight > el.clientHeight || 
                            el.scrollWidth > el.clientWidth
                        ) && style.overflow !== 'hidden' && style.display !== 'none';
                    });

                    // Scroll each element to its bottom or rightmost position
                    scrollableElements.forEach(el => {
                        el.scrollTop = el.scrollHeight; // Vertical scrolling
                        el.scrollLeft = el.scrollWidth; // Horizontal scrolling (if needed)
                    });
                """)
                # Optional: Wait briefly to ensure scrolling is applied
                time.sleep(0.2)
            except Exception as e:
                print(f"Error ensuring scroll behavior for all scrollable elements: {e}")
            
            # Capture a full-page screenshot
            screenshot = page.screenshot(full_page=True)
            image = Image.open(io.BytesIO(screenshot))
            frame = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            
            # Clean up
            context.close()
            self.browser.close()
            return frame




    def _capture_and_store_frame(self):
        """Capture the current state of the game as a frame"""
        if not self.record_video:
            return
            
        try:
            frame = self._capture_frame_with_playwright()
            self.frames.append(frame)
        except Exception as e:
            print(f"Error capturing frame: {e}")

    def _save_video(self):
        """Save the recorded frames as a video"""
        if not self.frames:
            return
            
        try:
            height, width = self.frames[0].shape[:2]
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            out = cv2.VideoWriter(
                self.video_path,
                fourcc,
                1.0,  # 1 FPS
                (width, height),
                True
            )
            
            for frame in self.frames:
                out.write(frame)
            
            out.release()
            
            # Try to re-encode with ffmpeg if available
            try:
                import subprocess
                temp_path = self.video_path + ".temp.mp4"
                os.rename(self.video_path, temp_path)
                subprocess.run([
                    'ffmpeg', '-i', temp_path,
                    '-c:v', 'libx264',
                    '-preset', 'medium',
                    '-crf', '18',
                    '-y',
                    self.video_path
                ])
                os.remove(temp_path)
            except:
                if os.path.exists(temp_path):
                    os.rename(temp_path, self.video_path)
            
            print(f"\nVideo saved to {self.video_path}")
            
        except Exception as e:
            print(f"Error saving video: {e}")

    def step(self, action: str):
        """Take a step and update the display"""
        current_player = self.env.state.current_player_id
        
        # Add action to chat history
        self.chat_history.append({
            "player_id": current_player,
            "message": action,
            "timestamp": time.time()
        })
        
        # Take the step
        done, info = self.env.step(action)
        self.renderer.chat_history = self.chat_history

        reward = self.env.close()
        
        # If game is over, set end game state
        if done:
            self.renderer.set_end_game_state(reward if reward else {}, info)
        
        # Update display
        self.renderer.draw()
        
        # Capture frame if recording
        if self.record_video:
            self._capture_and_store_frame()
        else:
            time.sleep(0.2)
        
        return done, info

    def reset(self, seed: Optional[int] = None):
        """Reset the environment and update the display"""
        obs = self.env.reset(seed)
        self.chat_history = []
        self.renderer.chat_history = []
        self.renderer.draw()
        
        if self.record_video:
            self._capture_and_store_frame()
            
        return obs

    def close(self):
        """Clean up resources"""
        if self.record_video:
            try:
                self._save_video()
            except Exception as e:
                print(f"Error during cleanup: {e}")

        # Clean up ngrok tunnel if it exists
        if NGROK_AVAILABLE and ngrok.get_tunnels():
            ngrok.disconnect_all()
            ngrok.kill()

    def __getattr__(self, name):
        """Delegate unknown attributes to the environment"""
        return getattr(self.env, name)