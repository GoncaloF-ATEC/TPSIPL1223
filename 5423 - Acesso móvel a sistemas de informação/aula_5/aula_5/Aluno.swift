//
//  Aluno.swift
//  aula_5
//
//  Created by Gonçalo Feliciano on 22/10/2024.
//

class Aluno: Pessoa{
    
    var turma: String
    
    init(nome: String, idade: Int, turma: String) {
        self.turma = turma
        super.init(nome: nome, idade: idade)
    }
    
    
    override func infos() -> String {
        "Aluno"
    }
}
