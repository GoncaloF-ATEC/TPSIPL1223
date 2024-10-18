//
//  main.swift
//  aula_4
//
//  Created by Gonçalo Feliciano on 18/10/2024.
//

import Foundation

// dict


var dict0:[String: String]

// a key tem de ser -> Hashable
var dict1 = [ "Key" : "Value"]

dict1["nova key"] = "novo valor"

print(dict1.keys)
print("-----")
print(dict1.values)
print("-----")
print(dict1.contains(where: { (key: String, value: String) in
    return key == "Key"
}))

print("-----")
for elm in dict1{
    
    print(elm.key)
}


print("-----")
for elm in dict1.values{
    
    print(elm)
}




print("-----")
for elm in dict1{
    
    print(elm.key)
}


print("-----")
dict1.forEach { (key, value) in
    print(key)
}


dict1["nova key"] = nil

print(dict1)


dict1 = [ "Key" : "Value"]
print(dict1["Key"]!)

// set

var mySet1 = Set<String>()

var mySet:Set = ["Ovos", "Polvilho", "Leite", "Sal", "Queijo"]

print(mySet)

print(mySet.contains("Ovos".capitalized))

print(mySet.count)

print(mySet)
var resp = mySet.insert("Oleo")

print(mySet)


print("-----")
print(resp)

resp = mySet.insert("Oleo")
print(resp)

print("-----")
for elm in mySet{
    print(elm)
}
print("-----")

mySet.forEach { elm in
    print(elm)
}
print("-----")


mySet1 = ["Ovos", "Farinha", "Açucar", "Iogurte", "Oleo" ]



print(mySet.union(mySet1))

//mySet.formUnion(mySet1)
//print(mySet)


print(mySet.symmetricDifference(mySet1))

print(mySet.intersection(mySet1))


print(mySet.subtracting(mySet1))
print(mySet1.subtracting(mySet))

// enum


enum grau{
    case cet
    case BSc
    case MSc
    case PHd
    case PosDoc
}

var bla = grau.BSc

print(bla == grau.MSc)


enum grau2: String{
    case cet = "cet"
    case BSc = "Lic"
    case MSc = "Mestredo"
    case PHd = "Doutorado"
    case posDoc = " Pos doutoramento"

}


var g = grau2.BSc

print(g == grau2.BSc)

print(grau2.MSc.rawValue)




print("-----")

var al = Aluno(nome: "nome do aluno", email: "nome@sapo.pt", idade: 15, altura: 1.5)

print(al.nome)
print(al)


var al2 = AlunoV2(nome: "nome do aluno", email: "nome@sapo.pt", idade: 15, altura: 1.5)


print(al2.nome)
print(al2)

print("-----")

var novo_al = al

print(al.nome)
print(novo_al.nome)

novo_al.nome = "João"
print("--")

print(al.nome)
print(novo_al.nome)

print("-----")


var novo_al2 = al2


print(al2.nome)
print(novo_al2.nome)

novo_al2.nome = "João"

print("--")
print(al2.nome)
print(novo_al2.nome)
