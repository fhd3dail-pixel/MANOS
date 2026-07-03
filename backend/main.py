#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
╔═══════════════════════════════════════════════════════════╗
║                    🤖 MANOS PLATFORM                      ║
║        منصة ذكية للاختبار الأخلاقي والتحليل الذكي       ║
║                                                           ║
║         صُنعت في العراق العظيم 🇮🇶                        ║
║      على يد: أمير الحشداوي (fhd3dail-pixel)              ║
║                                                           ║
║  الذكاء الاصطناعي الحر | اختبار الشبكات | التطوير الذاتي ║
╚═══════════════════════════════════════════════════════════╝
"""

import os
import sys
from pathlib import Path
from fastapi import FastAPI, UploadFile, File, WebSocket, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
import uvicorn
from datetime import datetime
import json

# إضافة المسارات
BACKEND_DIR = Path(__file__).parent
SYS_PATH = [str(BACKEND_DIR / 'src'), str(BACKEND_DIR)]
for path in SYS_PATH:
    if path not in sys.path:
        sys.path.insert(0, path)

# استيراد المكونات
try:
    from src.ai_engine import AIEngine
    from src.network_tools import NetworkTools
    from src.web_scraper import WebScraper
    from src.social_analyzer import SocialMediaAnalyzer
    from src.code_generator import CodeGenerator
    from src.self_update import SelfUpdateEngine
    from src.ai_control_panel import AIControlPanel
except ImportError as e:
    print(f"⚠️ تحذير: {e}")

# إنشاء التطبيق
app = FastAPI(
    title="🤖 MANOS - منصة الذكاء الحر",
    description="منصة مفتوحة مجانية 100% بدون قيود - صُنعت في العراق العظيم",
    version="1.0.0-FINAL",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# المتغيرات العامة
ai_engine = None
network_tools = None
web_scraper = None
social_analyzer = None
code_generator = None
self_updater = None
ai_panel = None

# ============ STARTUP ============

@app.on_event("startup")
async def startup_event():
    """تهيئة التطبيق"""
    global ai_engine, network_tools, web_scraper, social_analyzer, code_generator, self_updater, ai_panel
    
    print("""
    ╔════════════════════════════════════════════════════════════╗
    ║         🚀 MANOS PLATFORM - النسخة النهائية             ║
    ║                                                            ║
    ║         صُنعت في العراق العظيم 🇮🇶                        ║
    ║      على يد: أمير الحشداوي (fhd3dail-pixel)              ║
    ║                                                            ║
    ║    ✅ ذكاء اصطناعي حر 100% بدون قيود                     ║
    ║    ✅ تطوير ذاتي تلقائي                                  ║
    ║    ✅ لوحة تحكم ذكية                                     ║
    ║    ✅ مجاني بالكامل                                      ║
    ║                                                            ║
    ║    📍 http://localhost:8000                               ║
    ║    📚 http://localhost:8000/api/docs                      ║
    ╚════════════════════════════════════════════════════════════╝
    """)
    
    try:
        ai_engine = AIEngine()
        print("✅ محرك الذكاء الاصطناعي الحر: جاهز")
    except Exception as e:
        print(f"❌ خطأ: {e}")
    
    try:
        network_tools = NetworkTools()
        print("✅ أدوات الشبكات: جاهزة")
    except Exception as e:
        print(f"❌ خطأ: {e}")
    
    try:
        web_scraper = WebScraper()
        print("✅ أداة Web Scraping: جاهزة")
    except Exception as e:
        print(f"❌ خطأ: {e}")
    
    try:
        social_analyzer = SocialMediaAnalyzer()
        print("✅ محلل وسائل التواصل: جاهز")
    except Exception as e:
        print(f"❌ خطأ: {e}")
    
    try:
        code_generator = CodeGenerator()
        print("✅ مولد الأكواد: جاهز")
    except Exception as e:
        print(f"❌ خطأ: {e}")
    
    try:
        self_updater = SelfUpdateEngine()
        print("✅ نظام التحديث الذاتي: جاهز")
    except Exception as e:
        print(f"❌ خطأ: {e}")
    
    try:
        ai_panel = AIControlPanel()
        print("✅ لوحة تحكم الذكاء الاصطناعي: جاهزة")
    except Exception as e:
        print(f"❌ خطأ: {e}")
    
    print("\n✨ منصة MANOS جاهزة 100%!\n")

# ============ MAIN ROUTES ============

@app.get("/")
async def root():
    """الصفحة الرئيسية"""
    return {
        "status": "✅ MANOS Platform - Final Edition",
        "platform": "🤖 منصة MANOS الذكية",
        "made_in": "🇮🇶 العراق العظيم",
        "developer": "👤 أمير الحشداوي",
        "version": "1.0.0-FINAL",
        "free_tier": "✅ 100% مجاني وحر",
        "timestamp": datetime.now().isoformat(),
        "features": {
            "ai_unrestricted": "✅ ذكاء اصطناعي حر بدون قيود",
            "self_development": "✅ تطوير ذاتي تلقائي",
            "ai_dashboard": "✅ لوحة تحكم الذكاء الاصطناعي",
            "network_tools": "✅ أدوات اختبار الشبكات",
            "auto_updates": "✅ تحديثات مجانية تلقائية",
            "no_subscription": "✅ بدون اشتراكات",
            "no_ads": "✅ بدون إعلانات"
        }
    }

@app.get("/health")
async def health():
    """فحص صحة النظام"""
    return {"status": "healthy", "platform": "MANOS"}

# ============ AI ENDPOINTS - UNRESTRICTED ============

@app.post("/api/ai/chat")
async def ai_chat(message: str, language: str = "ar-IQ"):
    """محادثة ذكية بدون قيود"""
    if not ai_engine:
        raise HTTPException(status_code=503, detail="AI Engine unavailable")
    
    try:
        response = await ai_engine.chat(message, language)
        return {
            "status": "success",
            "message": message,
            "response": response,
            "language": language,
            "unrestricted": True,
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/ai/generate-code")
async def generate_code(language: str, description: str):
    """توليد أكواد بدون قيود"""
    if not code_generator:
        raise HTTPException(status_code=503, detail="Code Generator unavailable")
    
    try:
        code = await code_generator.generate(language, description)
        return {
            "status": "success",
            "language": language,
            "description": description,
            "code": code,
            "unrestricted": True
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/ai/generate-website")
async def generate_website(name: str, pages: int = 5):
    """توليد موقع ويب كامل"""
    if not code_generator:
        raise HTTPException(status_code=503, detail="Code Generator unavailable")
    
    try:
        result = await code_generator.generate_website(name, pages)
        return {
            "status": "success",
            "website": result,
            "unrestricted": True
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/ai/generate-app")
async def generate_app(framework: str, features: list):
    """توليد تطبيق كامل"""
    if not code_generator:
        raise HTTPException(status_code=503, detail="Code Generator unavailable")
    
    try:
        result = await code_generator.generate_app(framework, features)
        return {
            "status": "success",
            "app": result,
            "unrestricted": True
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/ai/generate-game")
async def generate_game(genre: str, features: list):
    """توليد لعبة كاملة"""
    if not code_generator:
        raise HTTPException(status_code=503, detail="Code Generator unavailable")
    
    try:
        result = await code_generator.generate_game(genre, features)
        return {
            "status": "success",
            "game": result,
            "unrestricted": True
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ============ AI CONTROL PANEL ============

@app.get("/api/ai/dashboard")
async def ai_dashboard():
    """لوحة تحكم الذكاء الاصطناعي"""
    if not ai_panel:
        raise HTTPException(status_code=503, detail="AI Panel unavailable")
    
    try:
        dashboard = await ai_panel.get_dashboard()
        return {
            "status": "success",
            "dashboard": dashboard,
            "free": True
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/ai/panel/settings")
async def ai_panel_settings(setting: str, value: any):
    """تعديل إعدادات الذكاء الاصطناعي"""
    if not ai_panel:
        raise HTTPException(status_code=503, detail="AI Panel unavailable")
    
    try:
        result = await ai_panel.update_setting(setting, value)
        return {
            "status": "success",
            "setting": setting,
            "value": value,
            "result": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/ai/panel/models")
async def ai_models():
    """قائمة نماذج الذكاء الاصطناعي المتاحة"""
    if not ai_panel:
        raise HTTPException(status_code=503, detail="AI Panel unavailable")
    
    try:
        models = await ai_panel.get_available_models()
        return {
            "status": "success",
            "models": models,
            "free": True
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ============ NETWORK TOOLS ============

@app.post("/api/network/scan")
async def network_scan(target: str):
    """مسح الشبكة"""
    if not network_tools:
        raise HTTPException(status_code=503, detail="Network Tools unavailable")
    
    try:
        results = await network_tools.scan(target)
        return {
            "status": "success",
            "target": target,
            "results": results,
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ============ SELF-UPDATE SYSTEM ============

@app.get("/api/system/updates")
async def check_updates():
    """فحص التحديثات المجانية"""
    if not self_updater:
        raise HTTPException(status_code=503, detail="Update Engine unavailable")
    
    try:
        updates = await self_updater.check_updates()
        return {
            "status": "success",
            "updates": updates,
            "free": True
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/system/auto-update")
async def auto_update():
    """تحديث تلقائي مجاني"""
    if not self_updater:
        raise HTTPException(status_code=503, detail="Update Engine unavailable")
    
    try:
        result = await self_updater.auto_update()
        return {
            "status": "success",
            "result": result,
            "free": True
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/system/self-improve")
async def self_improve():
    """تحسين ذاتي تلقائي"""
    if not self_updater:
        raise HTTPException(status_code=503, detail="Update Engine unavailable")
    
    try:
        improvements = await self_updater.self_improve()
        return {
            "status": "success",
            "improvements": improvements,
            "free": True
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/system/status")
async def system_status():
    """حالة النظام"""
    return {
        "platform": "MANOS",
        "version": "1.0.0-FINAL",
        "made_in": "🇮🇶 العراق العظيم",
        "developer": "👤 أمير الحشداوي",
        "status": "✅ شغال 100%",
        "free_tier": "✅ مجاني كاملاً",
        "timestamp": datetime.now().isoformat()
    }

# ============ ERROR HANDLERS ============

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """معالج الأخطاء العام"""
    return JSONResponse(
        status_code=500,
        content={
            "error": "خطأ في النظام",
            "details": str(exc),
            "timestamp": datetime.now().isoformat()
        }
    )

# ============ MAIN ============

if __name__ == "__main__":
    print("""
    ╔════════════════════════════════════════════════════════════╗
    ║                                                            ║
    ║         🚀 تشغيل منصة MANOS - النسخة النهائية            ║
    ║                                                            ║
    ║         صُنعت في العراق العظيم 🇮🇶                        ║
    ║      على يد: أمير الحشداوي (fhd3dail-pixel)              ║
    ║                                                            ║
    ║         ✅ ذكاء اصطناعي حر بدون قيود                     ║
    ║         ✅ تطوير ذاتي تلقائي                            ║
    ║         ✅ لوحة تحكم ذكية                               ║
    ║         ✅ 100% مجاني وحر                                ║
    ║                                                            ║
    ║         📍 http://localhost:8000                           ║
    ║         📚 http://localhost:8000/api/docs                  ║
    ║                                                            ║
    ╚════════════════════════════════════════════════════════════╝
    """)
    
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
