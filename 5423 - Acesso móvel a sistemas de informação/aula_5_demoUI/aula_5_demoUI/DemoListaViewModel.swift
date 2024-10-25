//
//  DemoListaViewModel.swift
//  aula_5_demoUI
//
//  Created by Gonçalo Feliciano on 25/10/2024.
//

import Foundation


class DemoListaViewModel:ObservableObject{
    @Published var lista = [
                            Pessoa(nome: "Ana"),
                            Pessoa(nome: "Bruno"),
                            Pessoa(nome: "Carla"),
                            Pessoa(nome: "Daniel"),
                            Pessoa(nome: "Eduarda"),
                            Pessoa(nome: "Fernando"),
                            Pessoa(nome: "Gabriela"),
                            Pessoa(nome: "Henrique"),
                            Pessoa(nome: "Isabela"),
                            Pessoa(nome: "João"),
                            Pessoa(nome: "Karina"),
                            Pessoa(nome: "Lucas"),
                            Pessoa(nome: "Mariana"),
                            Pessoa(nome: "Nicolas"),
                            Pessoa(nome: "Olivia")
                        ]
    
    
    @Published var novoNome:String = ""
    
    func addPessoa(){
        if !novoNome.isEmpty{
            self.lista.append(Pessoa(nome: novoNome))
        }
        novoNome = ""
        
    }
    
    
}
