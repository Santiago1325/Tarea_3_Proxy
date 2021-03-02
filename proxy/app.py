import proxy
import numero

proxy1 = proxy.Proxy(numero.Numero(2))
proxy2 = proxy.Proxy(numero.Numero(3))

print(proxy1.proxy())
print(proxy2.proxy())


