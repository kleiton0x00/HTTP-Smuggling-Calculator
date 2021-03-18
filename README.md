# TECL_DesyncCalculator

Perform TE.CL HTTP Request Smuggling attacks by crafting HTTP Request automatically.

A simple python script which allows you to customise both Normal request and Smuggled request and calculates the Content-Length and TE.CL Chunk which is crucial part during TE.CL Smuggling Exploit Development.

## Installation

```
git clone https://github.com/kleiton0x00/TECL_DesyncCalculator.git  
cd TECL_DesyncCalculator  
chmod +x TECL_DesyncCalculator.py  
python3 TECL_DesyncCalculator.py
```
## Usage

Follow the instructions and you will build the special-crafted HTTP Request. Just a few things to keep in mind:
- Host must be **without** http://
- For some extra TE Header obfuscation, you can use the alternative TE Headers:
```
Transfer-Encoding: xchunked

Transfer-Encoding : chunked

Transfer-Encoding: chunked\nTransfer-Encoding: x

Transfer-Encoding:\tchunked

Transfer-Encoding\t:\tchunked

 Transfer-Encoding: chunked

X: X\nTransfer-Encoding: chunked

Transfer-Encoding\n : chunked
```

- HTTP Method can be: POST, GET, OPTIONS, PUT, DELETE and so on...  
- The directory can be **/** or **/directory** or it can be an endpoint with parameter **/index.php?id=1**  
- HTTP Protocol can be **HTTP/1.1** or **HTTP/2**  

**Note:** If you want to add more headers, you can uncomment the following lines **41-44**. If you want to add your own headers, follow the rules below:
- To add additional **Normal** request:  
```smuggle += "your new header" + RN```

- To add additional **Smuggled** request:  
```prefix += "your new header" + RN```

## Articles

Here is my article where I used this tool to exploit TE.CL vulnerability: https://kleiton0x00.github.io/posts/Exploiting-HTTP-Request-Smuggling-(TE.CL)-XSS-to-website-takeover/

## Credits:
A huge thanks goes to [@defparam](https://github.com/defparam/tiscripts) repository for making this possible and a huge thanks to the original author of HTTP Request smuggling for the Obfuscated TE Headers on [this article](https://portswigger.net/research/http-desync-attacks-request-smuggling-reborn)
