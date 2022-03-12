# HTTP CL.TE & TE.CL Desync Calculator

Perform CL.TE and TE.CL HTTP Request Smuggling attacks by crafting HTTP Request automatically.

A simple python script which allows you to customise both Normal request and Smuggled request and calculates the Content-Length and TE.CL Chunk which is crucial part during the Smuggling Exploit Development.

## Installation

```
git clone https://github.com/kleiton0x00/HTTP-Smuggling-Calculator.git  
cd HTTP-Smuggling-Calculator
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
- HTTP Protocol can only be **HTTP/1.1** (HTTP/2 protocol is a whole another story) 

## CL.TE usage
- To add headers in the smuggled request (line 75):  
```smuggle += "My Header: my value" + RN```

- To add body request in the smuggled request (line: 58):  
```smuggle_body += "search=kleiton0x7e&id=1" + RN```

- To add headers in the normal request (line: 89):  
```regular += "My header: my value" + RN```

## TE.CL usage
**Note:** If you want to add more headers, you can uncomment the following lines **41-44**. If you want to add your own headers, follow the rules below:
- To add headers **Normal** request:  
```smuggle += "My header: my value" + RN```

- To add headers in the  **Smuggled** request:  
```prefix += "My header: my value" + RN```

## Articles

Here is my article where I used this tool to exploit TE.CL vulnerability: https://kleiton0x00.github.io/posts/Exploiting-HTTP-Request-Smuggling-(TE.CL)-XSS-to-website-takeover/

## Credits:
A huge thanks goes to [@defparam](https://github.com/defparam/tiscripts) repository for making this possible and a huge thanks to the original author of HTTP Request smuggling for the Obfuscated TE Headers on [this article](https://portswigger.net/research/http-desync-attacks-request-smuggling-reborn)
