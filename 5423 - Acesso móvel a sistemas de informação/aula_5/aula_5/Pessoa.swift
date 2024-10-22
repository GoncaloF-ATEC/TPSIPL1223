//
//  Pessoa.swift
//  aula_5
//
//  Created by Gonçalo Feliciano on 22/10/2024.
//

class Pessoa{
    
    var nome: String
    var idade: Int
    
    init(nome: String, idade: Int) {
        self.nome = nome
        self.idade = idade
    }
    

    
    func envelhercer(anos: Int = 1){
        self.idade += anos
    }
    
    
    
    final func infos2() -> String{
        return "Pessoa"
    }
    
    func infos() -> String{
        return "Pessoa"
    }
    
}
