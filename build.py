import sys, os, json

logo = """
# -----------------------------------------------------------
#  _____                _           _            _ _   _         
# /  __ \              | |         | |          (_) | | |        
# | /  \/_ __ ___  __ _| |_ ___  __| | __      ___| |_| |__      
# | |   | '__/ _ \/ _` | __/ _ \/ _` | \ \ /\ / / | __| '_ \     
# | \__/\ | |  __/ (_| | ||  __/ (_| |  \ V  V /| | |_| | | |    
#  \____/_|  \___|\__,_|\__\___|\__,_|   \_/\_/ |_|\__|_| |_|    
                                                                                                                 
#  _   _                   _____                    _             
# | | | |                 |  ___|                  | |            
# | |_| |__   ___  __   _ |___ \   _ __   __ _  ___| | _____ _ __ 
# | __| '_ \ / _ \ \ \ / /    \ \ | '_ \ / _` |/ __| |/ / _ \ '__|
# | |_| | | |  __/  \ V / /\__/ / | |_) | (_| | (__|   <  __/ |   
#  \__|_| |_|\___|   \_/  \____/  | .__/ \__,_|\___|_|\_\___|_|   
#                                 | |                             
#                                 |_|                 
# -----------------------------------------------------------\n\n\n\n\n\n\n\n\n\n\n\n
"""

def findall(p, s):
    '''Yields all the positions of
    the pattern p in the string s.'''
    i = s.find(p)
    while i != -1:
        yield i
        i = s.find(p, i+1)

path = sys.argv[1]
os.chdir(path)
if "TEMPLATE.py" in os.listdir(path):
    f = open(os.path.join(path, "TEMPLATE.py"), "r")
    template = logo+f.read()


    f.close()
    baseProdj = None
    outdir = ""

    if "#!base" in template:
        outdir = template.split("#!base ")[1].split('\n')[0]
        baseProdj = json.load(open(
                outdir
            , 'r'))
        if baseProdj.get("mode", "NONE") != "Text":
            print("Error!!! #!base must be a text projects")
            exit()
    else:
        print("Error!!! #!base required")
        exit()

    if '#!out' in template:
        outdir=template.split("#!out ")[1].split('\n')[0]

    while '#!dump ' in template:
        dp = template.split('#!dump ')[1].split('\n')[0]
        f = open(dp, "r")
        d = f.read()
        f.close()
        template=template.replace(dp, dp+"\n"+d+"\n", 1)

        template=template.replace('#!dump ', '# !dump ', 1)
    
    template=template.replace('#!ignoreNextLine\n', '#!ignoreNextLine\n#')



    baseProdj["textContent"] = template
    f = open(outdir, "w")
    f.write(json.dumps(baseProdj))
    f.close()
    


else:
    print("Error!!! TEMPLATE.py not found")