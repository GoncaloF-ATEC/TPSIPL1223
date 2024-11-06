//
//  Pessoa.swift
//  Listas_vs
//
//  Created by Gonçalo Feliciano on 06/11/2024.
//

import Foundation


class Pessoa:Identifiable, Equatable, Comparable{

    
    
    var id = UUID()
    var nome:String
    var tlm:String
    
    init(nome: String, tlm: String) {
        self.nome = nome
        self.tlm = tlm
    }
    
    
    static func == (lhs: Pessoa, rhs: Pessoa) -> Bool {
        lhs.nome == rhs.nome
    }
    
    static func < (lhs: Pessoa, rhs: Pessoa) -> Bool {
        lhs.nome < rhs.nome
    }
    
    func starts(with c:String) -> Bool{
        nome.lowercased().starts(with: c.lowercased())
    }
    
}
