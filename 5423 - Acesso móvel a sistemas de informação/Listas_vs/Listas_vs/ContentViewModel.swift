//
//  ContentViewModel.swift
//  Listas_vs
//
//  Created by Gonçalo Feliciano on 06/11/2024.
//

import Foundation

class ContentViewModel:ObservableObject{
    
    
    @Published var pessoas: [Pessoa] = [
        Pessoa(nome: "Ana", tlm: "912345678"),
        Pessoa(nome: "Bruno", tlm: "923456789"),
        Pessoa(nome: "Carlos", tlm: "934567890"),
        Pessoa(nome: "Diana", tlm: "945678901"),
        Pessoa(nome: "Eduardo", tlm: "956789012")
    ]
    
    
    func nomesComecados(com c: String) -> [Pessoa]{
        self.pessoas.filter { p in
            p.starts(with: "A")
        }
    
    }
    
    
    
    
    
    
    
}
