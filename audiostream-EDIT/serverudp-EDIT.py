import socket
import soundcard as sc
import numpy as np

# --- CONFIGURATION ---
TARGET_IP = '192.168.1.255' 
CLIENT_PORT = 5005
SAMPLE_RATE = 44100
CHUNK = 512 

# --- VOLUME CONTROL ---
# 1.0 = Original Volume
# 0.1 = Very Quiet
# 1.5 = Boosted (May cause distortion if original audio is loud)
VOLUME_FACTOR = 0.2
 

def start_streaming():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    if TARGET_IP.endswith('.255'):
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    try:
        speaker = sc.default_speaker()
        mic = sc.get_microphone(id=str(speaker.name), include_loopback=True)
        
        print(f"[*] Streaming with Volume Multiplier: {VOLUME_FACTOR}")

        with mic.recorder(samplerate=SAMPLE_RATE) as recorder:
            while True:
                data = recorder.record(numframes=CHUNK)
                
                # Convert Stereo to Mono
                mono_data = np.mean(data, axis=1)
                
                # --- APPLY VOLUME CONTROL ---
                # We multiply the raw floats before converting to Int16
                controlled_data = mono_data * VOLUME_FACTOR
                
                # Scale to 16-bit and CLIP to prevent "rollover" noise
                pcm_floats = controlled_data * 32767
                pcm_final = np.clip(pcm_floats, -32768, 32767).astype(np.int16)
                
                sock.sendto(pcm_final.tobytes(), (TARGET_IP, CLIENT_PORT))

    except KeyboardInterrupt:
        print("\n[*] Stopped.")
    finally:
        sock.close()

if __name__ == "__main__":
    start_streaming()