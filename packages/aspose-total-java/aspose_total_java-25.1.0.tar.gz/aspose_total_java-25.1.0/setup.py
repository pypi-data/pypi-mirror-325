from setuptools import setup

NAME = "aspose-total-java"
VERSION = "25.1.0"
REQUIRES = ["aspose-barcode-for-python-via-java==25.1.0",
            "aspose-cells==25.1.0",
            "aspose-diagram==25.1.0",
            "aspose-ocr-python-java==24.7.0",
            "aspose-pdf-for-python-via-java==24.9",
            # Resolving JPype1 dependency conflicts
            "JPype1>=1.2.1,<1.6.0"  # Compatible range covering all conflicting versions
            ]

setup(
    name=NAME,
    version=VERSION,
    description='Aspose.Total for Python via Java is a file format Processing python class library that allows developers to work with Microsoft Excel®, Microsoft Visio®, and barcode file formats without needing Office Automation.',
    keywords=["XLS","XLSX","XLSB","XLTX","XLTM","XLSM","XML","ODS","CSV","TSV","TXT","HTML","MHTML","PDF","PDF/A","XPS","JPEG","PNG","BMP","SVG","EMF","GIF","VSDX","VDX","VSX","VTX","VSSX","VSTX","VSDM","VSSM","VSTM","XAML","On Premise API","High Code API","API","Spreadsheets","Excel","Barcode","1D Barcode","2D Barcode","Python Java","Diagram","Visio","Barcode Generation","Barcode Recognition","Read","Write","Export","Worksheet","Render","Text","Image","Scan","High Fidelity","Shapes","File Format","Symbologies","Codabar","Code Text","QR Code","Pivot Table","Pivot Charts","DataMatrix","Aztec","Pdf417","MacroPdf417"],
    url='https://products.aspose.com/total/python-java',
    author='Aspose',
    author_email='total@aspose.com',
    packages=['aspose-total-java'],
    include_package_data=True,
    long_description=open("README.md", encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    install_requires=REQUIRES,
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'License :: Other/Proprietary License'
    ],
    platforms=[
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows :: Windows 7',
        'Operating System :: Microsoft :: Windows :: Windows Vista',
        'Operating System :: POSIX :: Linux',
    ],
    python_requires='>=3.5',
)
