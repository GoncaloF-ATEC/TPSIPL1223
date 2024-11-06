//
//  ContentView.swift
//  Listas_vs
//
//  Created by Gonçalo Feliciano on 06/11/2024.
//

import SwiftUI

struct ContentView: View {
    
    @StateObject var vm = ContentViewModel()
    
    var body: some View {
        List {
            
            
            Section{
                
                ForEach(vm.nomesComecados(com: "A")){ elm in
                    
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
