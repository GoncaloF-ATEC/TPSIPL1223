//
//  main.swift
//  aula_5
//
//  Created by Gonçalo Feliciano on 22/10/2024.
//

import Foundation



var al = Aluno(nome: "Nome Aluno", idade: 23, turma: "TPSI")
var p = Pessoa(nome: "Nome Pessoa", idade: 30)
var prof = Professor(nome: "nome Porfessor", idade: 34, grau: Grau.PHd) // Professor(nome: "nome Porfessor", idade: 34, grau: .PHd)


var lista = [al, p, prof]


for i in lista{
    if i is Professor {
        var prof2 = i as! Professor
        print(prof2.grau)
    }
    
}

print("--------")

for i in lista{
    
    if let myPorf = i as? Professor{
        print(myPorf.grau)
    }
    
}

print("--------")
print("--------")


var l = [13,424,42,42,432,4324]


print(l.avg)

