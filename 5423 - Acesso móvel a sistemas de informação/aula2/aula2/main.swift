//
//  main.swift
//  aula2
//
//  Created by Gonçalo Feliciano on 19/09/2024.
//

import Foundation

// tuplos

var info = ("Gonçalo", 2022, true)

print(info.0)
print(info.1)
print(info.2)

info.2 = false

print(info.2)

print("------------")
var infoV2 = (nome: "Gonçalo", inicio: 2022, ativo: true)

print(infoV2.0)
print(infoV2.1)
print(infoV2.2)

print("----")
print(infoV2.nome)
print(infoV2.inicio)
print(infoV2.ativo)


var infoV3: (String, Int, Bool)

infoV3 = ("Gonçalo", 2022, true)
print(infoV3.1)

infoV3  = (nome: "Gonçalo", inicio: 2022, ativo: true)
print(infoV3.2)



var infoV4: (nome:String, inicio:Int, ativo:Bool)

infoV4 = ("Gonçalo", 2022, true)
print(infoV4.ativo)


infoV4 = (nome: "Gonçalo", inicio: 2022, ativo: true)
print(infoV4.ativo)

//nfoV4 = (foo: "Gonçalo", boo: 2022, roo: true)
//print(infoV4.ativo)


infoV4 = (inicio: 2022, nome: "Gonçalo",  ativo: true)
print(infoV4.ativo)


// func


func func1(){
    print("ola Mundo func1")
}

func1()



func func2() -> String{
    return "ola Mundo func2"
}
print(func2())


func func3() -> String{
     "ola Mundo func3"
}

print(func3())


func func4(nome: String) -> String{
    "ola Mundo func4, \(nome)!!"
}


print(func4(nome: "Gonçalo"))


func func5(nome n: String) -> String{
    "ola Mundo func5, \(n)!!"
}


print(func5(nome: "Gonçalo"))


func func6(_ nome: String) -> String{
    "ola Mundo func6, \(nome)!!"
}

print(func6("Gonçalo"))


func _soma(valA: Int, valB:Int) -> Int{
    valA + valB
}

print(_soma(valA: 10, valB: 10))


func soma(_ valA: Int, com valB:Int) -> Int{
    valA + valB
}

print(soma(10, com: 10))
