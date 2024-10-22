//
//  Professor.swift
//  aula_5
//
//  Created by Gonçalo Feliciano on 22/10/2024.
//



class Professor: Pessoa{
    
    var grau:Grau
    
    init(nome: String, idade: Int, grau: Grau = .BSc) {
        self.grau = grau
        super.init(nome: nome, idade: idade)
    }
    
    
    
    override func infos() -> String {
        "Professor"
    }
    
}
