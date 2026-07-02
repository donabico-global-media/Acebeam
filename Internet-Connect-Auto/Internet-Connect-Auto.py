# -*- coding: utf-8 -*-
import os
from datetime import datetime

class EHCInternetConnectAuto:
    def __init__(self):
        self.log_file = "Connection-Log.txt"
        
    def launch_ocean_pulse(self):
        # Ghi lại trạng thái vào file trong kho
        log_entry = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] SYSTEM_SIGNAL: ACTIVE_SUCCESS\n"
        
        try:
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(log_entry)
            print(f"[SUCCESS] ✅ Ghi nhận nhật ký thành công: {log_entry.strip()}")
        except Exception as e:
            print(f"[ERROR] Không thể ghi log: {str(e)}")

if __name__ == "__main__":
    EHCInternetConnectAuto().launch_ocean_pulse()
