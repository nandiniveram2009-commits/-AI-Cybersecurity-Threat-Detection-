"""
Master Orchestration Script for AI-Powered Cybersecurity Threat Detection System.
"""

from src.preprocessing import load_and_preprocess_data
from src.train import train_models
from src.predict import simulate_realtime_prediction
from src.visualize import generate_visualizations

def main():
    print("==================================================")
    print("  AI-POWERED CYBERSECURITY THREAT DETECTION SYSTEM")
    print("==================================================")
    
    print("\n[Phase 1] Loading and Preprocessing Data...")
    load_and_preprocess_data()
    
    print("\n[Phase 2] Training Machine Learning Models...")
    train_models()
    
    print("\n[Phase 3] Running Real-Time Threat Detection Simulation...")
    simulate_realtime_prediction()
    
    print("\n[Phase 4] Generating Security Analytics & Visualizations...")
    generate_visualizations()
    
    print("\n==================================================")
    print("  PIPELINE COMPLETED SUCCESSFULLY. READY FOR GITHUB!")
    print("==================================================")

if __name__ == "__main__":
    main()
