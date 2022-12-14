const express= require("express");
const { generateFile}= require("./generateFile");
const { executeCpp }= require("./executeCpp");
const app = express();
app.use(express.urlencoded({extended:true}));
app.use(express.json());

app.get("/",(req,res)=>{
    return res.json({hello:"world"});
});
app.post("/run",async(req,res)=>{
    
    const {language = "cpp",code}= req.body;
    if (code === undefined){
        return res.status(400).json({sucess: false,error:"Empty code body!"})
    }
    try{
    //need to genrate a c++
    const filepath = await generateFile(language,code);
    //run file
    const output = await executeCpp(filepath);
    return res.json({filepath,output});
    }
    catch(err){
        res.status(500).json({err})
    }
    
})
app.listen(5000,()=>{
    console.log('listening port 5000');
});