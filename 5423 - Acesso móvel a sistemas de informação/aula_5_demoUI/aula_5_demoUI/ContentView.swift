//
//  ContentView.swift
//  aula_5_demoUI
//
//  Created by Gonçalo Feliciano on 22/10/2024.
//

import SwiftUI

struct ContentView: View {
    
    @StateObject var vm = ContentViewModel()
    
    var body: some View {
        NavigationStack{
            
            VStack{
                
                Text("\(vm.nome) - \(vm.num)")
                
                TextField("Nome", text: self.$vm.nome_tf)
                    .frame(width: 200)
                    .textFieldStyle(.roundedBorder)
                
                Spacer()
                    .frame(height: 40)
                
                Button {
                    
                    vm.btnMudarNome()
                    
                    
                } label: {
                    btnView(txt: "Btn1")
                }
                
                Spacer()
                    .frame(height: 40)
                
                NavigationLink {
                    
                    newView(nome: vm.nome, num: $vm.num)
                    
                } label: {
                    Text("Go to view 2")
                }

                
            } // main VStack
            .navigationTitle("Pag 1")
            .navigationBarTitleDisplayMode(.inline)
        } // NavigationStack
    }
}

#Preview {
    ContentView()
}

//mongoDB
// redis
//




/*
  
 
 intro swiftUI
        vistas
        multiplos files
        btns
        MVVM
        nav
        listas
    
 
31- img
    grids
    

 ?? -
 
 
?? cirar apis
        mongoDB
 
 
?? - ler e ecrever APIs
    

 

 
 
 
 
 
 */
