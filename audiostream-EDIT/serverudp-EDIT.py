import socket
import soundcard as sc
import numpy as np
import sys
import time

# --- KONFIGURASI ---
TARGET_IP = '192.168.1.255'  # Ganti dengan IP ESP32 jika ingin lebih stabil
CLIENT_PORT = 5005
SAMPLE_RATE = 44100
CHUNK = 512 
VOLUME_FACTOR = 0.2 

def start_streaming():
    # Setup UDP Socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    if TARGET_IP.endswith('.255'):
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    print(f"[*] Menghubungkan ke: {TARGET_IP}:{CLIENT_PORT}")
    print("[*] Visualizer Aktif. Tekan CTRL + C untuk berhenti.\n")
    print("  VOLUME LEVEL VISUALIZER")
    print("  " + "-" * 40)

    try:
        # Ambil speaker default dan loopback-nya
        speaker = sc.default_speaker()
        mic = sc.get_microphone(id=str(speaker.name), include_loopback=True)

        with mic.recorder(samplerate=SAMPLE_RATE) as recorder:
            while True:
                # 1. Rekam audio dari PC
                data = recorder.record(numframes=CHUNK)
                
                # 2. Proses Audio (Stereo -> Mono & Gain)
                mono_data = np.mean(data, axis=1)
                controlled_data = mono_data * VOLUME_FACTOR
                
                # 3. Visualizer di CMD (Tanda #)
                rms = np.sqrt(np.mean(controlled_data**2))
                bar_length = int(rms * 150) # Sensitivitas bar
                bar = '#' * min(bar_length, 40)
                
                # Menampilkan bar di baris yang sama (\r)
                # {bar:<40} memastikan lebar kolom tetap 40 karakter
                sys.stdout.write(f"\r  [{bar:<40}] {int(rms*100):3d}% ")
                sys.stdout.flush()

                # 4. Konversi ke PCM 16-bit dan Kirim ke ESP32
                pcm_floats = controlled_data * 32767
                pcm_final = np.clip(pcm_floats, -32768, 32767).astype(np.int16)
                sock.sendto(pcm_final.tobytes(), (TARGET_IP, CLIENT_PORT))

    except KeyboardInterrupt:
        # Bagian ini menangkap CTRL + C
        print("\n\n" + "="*50)
        print("[*] Program dihentikan oleh pengguna (CTRL+C).")
        print("[*] Menutup koneksi...")
    except Exception as e:
        print(f"\n[!] Terjadi Error: {e}")
    finally:
        sock.close()
        print("[*] Selesai. Sampai jumpa!")

if __name__ == "__main__":
    start_streaming()
