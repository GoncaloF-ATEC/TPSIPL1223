//
//  ContentView.swift
//  Listas_vs
//
//  Created by Gonçalo Feliciano on 06/11/2024.
//

import SwiftUI

struct ContentView: View {
    
    @State var pessoas: [Pessoa] = [
        Pessoa(nome: "Ana", tlm: "912345678"),
        Pessoa(nome: "Bruno", tlm: "923456789"),
        Pessoa(nome: "Carlos", tlm: "934567890"),
        Pessoa(nome: "Diana", tlm: "945678901"),
        Pessoa(nome: "Eduardo", tlm: "956789012")
    ]
    
    var body: some View {
        List {
            
            
            Section{
                
                ForEach(self.pessoas.filter { p in
                    p.starts(with: "A")
                }){ elm in
                    
                    Text(elm.nome)
                }
                
            } header: {
                Text("A")
            }
            
            
            
            
          
        }//List
        .listRowSpacing(5)
        .listStyle(.grouped)
    }//body: some view
}

#Preview {
    ContentView()
}
