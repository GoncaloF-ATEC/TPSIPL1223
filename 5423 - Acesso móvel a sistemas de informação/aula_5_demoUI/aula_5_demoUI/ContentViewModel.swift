//
//  ContentViewModel.swift
//  aula_5_demoUI
//
//  Created by Gonçalo Feliciano on 25/10/2024.
//

import SwiftUI

class ContentViewModel: ObservableObject{
    
    @Published var nome = "Gonçalo"
    @Published var nome_tf = ""
    @Published var num = 0
    
    
    func btnMudarNome(){
        
        
        if !nome_tf.isEmpty{
            nome = nome_tf
        }
        nome_tf = ""
        
    }

}

