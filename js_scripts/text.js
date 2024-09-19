const fs = require('fs');
const pdf = require('pdf-parse');
const Tesseract = require('tesseract.js');

async function extractPdfText(filePath) {
    const dataBuffer = fs.readFileSync(filePath);
    const data = await pdf(dataBuffer);
    
    console.log('Extracted Text from PDF:', data.text);

    // Optional: Perform OCR if text extraction is incomplete
    Tesseract.recognize(
        filePath,
        'ben', // Bengali language code
        {
            logger: info => console.log(info)
        }
    ).then(({ data: { text } }) => {
        console.log('OCR Text:', text);
    });
}

extractPdfText('../scripts/pypdf.pdf');
