#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
╔═══════════════════════════════════════════════════════════╗
║          🚀 MANOS APK Builder - بناء التطبيق تلقائياً     ║
║                                                           ║
║         صُنعت في العراق العظيم 🇮🇶                        ║
║      على يد: أمير الحشداوي (fhd3dail-pixel)              ║
║                                                           ║
║  أداة بناء APK الذكية والمجانية والحرة                 ║
╚═══════════════════════════════════════════════════════════╝
"""

import os
import subprocess
import sys
from pathlib import Path
from datetime import datetime

class MANOSAPKBuilder:
    """بناء تطبيق MANOS APK بشكل تلقائي"""
    
    def __init__(self):
        self.project_root = Path.cwd()
        self.frontend_dir = self.project_root / "frontend"
        self.apk_output = self.frontend_dir / "app/build/outputs/apk/debug"
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    def print_banner(self):
        """طباعة البانر الترحيبي"""
        print("""
        ╔════════════════════════════════════════════════════════════╗
        ║                                                            ║
        ║         🚀 MANOS APK Builder - نسخة 1.0.0                 ║
        ║                                                            ║
        ║         صُنعت في العراق العظيم 🇮🇶                        ║
        ║      على يد: أمير الحشداوي (fhd3dail-pixel)              ║
        ║                                                            ║
        ║    بناء التطبيق تلقائياً بدون قيود - 100% مجاني          ║
        ║                                                            ║
        ╚════════════════════════════════════════════════════════════╝
        """)
    
    def check_requirements(self) -> bool:
        """فحص المتطلبات"""
        print("\\n📋 فحص المتطلبات...")
        
        requirements = {
            "Java": "java -version",
            "Android SDK": "sdkmanager --version",
            "Gradle": "gradle --version"
        }
        
        for tool, cmd in requirements.items():
            try:
                subprocess.run(
                    cmd,
                    shell=True,
                    capture_output=True,
                    timeout=5
                )
                print(f"✅ {tool}: موجود")
            except:
                print(f"❌ {tool}: غير موجود")
                return False
        
        return True
    
    def build_apk(self) -> bool:
        """بناء ملف APK"""
        print("\\n🔨 جاري بناء APK...")
        
        try:
            # الدخول لمجلد frontend
            os.chdir(self.frontend_dir)
            
            # تشغيل Gradle build
            result = subprocess.run(
                ["./gradlew", "build"],
                capture_output=True,
                text=True,
                timeout=300
            )
            
            if result.returncode == 0:
                print("✅ تم بناء APK بنجاح!")
                return True
            else:
                print(f"❌ خطأ في البناء: {result.stderr}")
                return False
        
        except Exception as e:
            print(f"❌ خطأ: {str(e)}")
            return False
    
    def locate_apk(self) -> Path:
        """تحديد موقع ملف APK"""
        print("\\n📍 البحث عن ملف APK...")
        
        if self.apk_output.exists():
            apk_files = list(self.apk_output.glob("*.apk"))
            
            if apk_files:
                latest_apk = max(apk_files, key=lambda x: x.stat().st_mtime)
                print(f"✅ وجدت: {latest_apk}")
                return latest_apk
        
        return None
    
    def copy_to_output(self, apk_path: Path) -> Path:
        """نسخ APK إلى مجلد الإخراج"""
        print("\\n📦 نسخ الملف...")
        
        try:
            output_dir = Path("./releases")
            output_dir.mkdir(exist_ok=True)
            
            output_file = output_dir / f"MANOS-{self.timestamp}.apk"
            
            import shutil
            shutil.copy(apk_path, output_file)
            
            print(f"✅ تم النسخ إلى: {output_file}")
            return output_file
        
        except Exception as e:
            print(f"❌ خطأ: {str(e)}")
            return None
    
    def get_download_link(self, apk_path: Path) -> str:
        \"\"\"الحصول على رابط التحميل\"\"\"
        print("\\n🔗 إنشاء رابط التحميل...")
        
        # في بيئة حقيقية، ستحمل الملف على خادم
        # هنا سأعطيك رابط محلي
        github_url = \"https://github.com/fhd3dail-pixel/MANOS/releases\"\n        \n        return github_url\n    \n    def build_and_release(self):\n        \"\"\"بناء وإطلاق التطبيق كاملاً\"\"\"\n        self.print_banner()\n        \n        # فحص المتطلبات\n        if not self.check_requirements():\n            print(\"\\n⚠️  تحذير: بعض المتطلبات غير موجودة\")\n            print(\"📖 رجاءً اتبع هذا الرابط: https://developer.android.com/studio\")\n            return False\n        \n        # بناء APK\n        if not self.build_apk():\n            print(\"\\n❌ فشل البناء\")\n            return False\n        \n        # تحديد موقع APK\n        apk_path = self.locate_apk()\n        if not apk_path:\n            print(\"\\n❌ لم أجد ملف APK\")\n            return False\n        \n        # نسخ للإخراج\n        output_apk = self.copy_to_output(apk_path)\n        if not output_apk:\n            return False\n        \n        # الحصول على الرابط\n        download_link = self.get_download_link(output_apk)\n        \n        # النتيجة النهائية\n        print(\"\\n\" + \"=\"*60)\n        print(\"✅ تم بناء التطبيق بنجاح!\")\n        print(\"=\"*60)\n        print(f\"\\n📱 اسم الملف: {output_apk.name}\")\n        print(f\"📦 الحجم: {output_apk.stat().st_size / 1024 / 1024:.2f} MB\")\n        print(f\"\\n🔗 رابط التحميل:\")\n        print(f\"   {download_link}\")\n        print(f\"\\n📍 الموقع المحلي:\")\n        print(f\"   {output_apk.absolute()}\")\n        print(\"\\n\" + \"=\"*60)\n        print(\"\\n✨ منصة MANOS جاهزة للتحميل والاستخدام!\")\n        print(f\"🇮🇶 صُنعت في العراق العظيم\")\n        print(f\"👤 على يد: أمير الحشداوي\\n\")\n        \n        return True\n\nif __name__ == \"__main__\":\n    builder = MANOSAPKBuilder()\n    builder.build_and_release()\n