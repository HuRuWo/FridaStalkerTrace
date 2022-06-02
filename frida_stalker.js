

function hook_native() {
    var method_addr = Module.findExportByName("libnative.so")
    console.log('addr:'+method_addr)
    if(method_addr){
        Interceptor.attach(method_addr,{
            onEnter:function(args){
        
            },
            onLeave:function(retval){ 

            }
        })
    }
}


function main() {
    hook_native();
}

setImmediate(main);

// com.huruwo.testndk
// frida -U com.huruwo.testndk -l frida_stalker.js

//frida -U com.huruwo.testndk -l frida_stalker.js
//frida -U --no-pause -f  com.huruwo.testndk -l frida_stalker.js