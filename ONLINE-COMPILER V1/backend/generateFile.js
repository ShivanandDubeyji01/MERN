const path = require('path');
const fs = require('fs');
const { v4: uuid} = require('uuid')
const dirCode = path.join(__dirname,"codes");
if(!fs.existsSync(dirCode)){
    fs.mkdirSync(dirCode,{recursive:true})
}

const generateFile= async(format, content) =>{
    const jobId = uuid();
    const filename =`${jobId}.${format}`
    const filepath = path.join(dirCode, filename);
    await fs.writeFileSync(filepath, content);
    return filename;

};

module.exports={
    generateFile,
}