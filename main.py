import dashboard
import sys

if __name__ == "__main__":
    if "streamlit" not in sys.modules:
        print("Este dashboard debe ejecutarse con: streamlit run main.py")
    else:
        dashboard.run()
