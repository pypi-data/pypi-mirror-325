from setuptools import setup

setup(
    name="media_control",
    version="0.0.1",
    description="Application to access media controls on your device",
    author="sleepingsaint",
    url="https://github.com/sleepingsaint/media_control",
    include_package_data=True,
    install_requires=[
        "Flask",
        "flask-socketio",
        "pyautogui",
        "pillow",
        "qrcode",
        "volume-control"
    ],
    entry_points={
        'console_scripts': ['media_control=media_control.__init__:main']
    }, 
)