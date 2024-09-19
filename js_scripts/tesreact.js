const Tesseract = require('tesseract.js');
const path = require('path');

// Path to the image file (replace with your image path)
const image = path.resolve(__dirname, './output/page-1.png'); // Use the PNG generated from the PDF

Tesseract.recognize(
  image, 
  'ben',  // Specify Bangla (ben) as the language
  {
    logger: info => console.log(info), // Optional logging
  }
)
.then(({ data: { text } }) => {
  console.log('Recognized Text:', text);

  // You can save this output to a file if needed
  const fs = require('fs');
  fs.writeFileSync('output_bangla_text.txt', text, 'utf8');
})
.catch(err => {
  console.error('Error:', err);
});
