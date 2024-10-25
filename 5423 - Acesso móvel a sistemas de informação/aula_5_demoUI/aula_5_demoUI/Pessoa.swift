//
//  Pessoa.swift
//  aula_5_demoUI
//
//  Created by Gonçalo Feliciano on 25/10/2024.
//

import Foundation


class Pessoa: Identifiable{
    var id = UUID()
    var nome:String
    
    init(nome: String) {
        self.nome = nome
    }
    
    
    
}
