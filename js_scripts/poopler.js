const pdfPoppler = require('pdf-poppler');

const file = '../scripts/pypdf.pdf';
const opts = {
    format: 'png',
    out_dir: './output',
    out_prefix: 'page',
    page: null
};

pdfPoppler.convert(file, opts)
    .then(() => {
        console.log('Conversion complete');
    })
    .catch(error => {
        console.error(error);
    });
