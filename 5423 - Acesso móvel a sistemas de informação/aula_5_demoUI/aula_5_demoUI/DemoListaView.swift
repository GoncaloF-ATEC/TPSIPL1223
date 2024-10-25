//
//  DemoListaView.swift
//  aula_5_demoUI
//
//  Created by Gonçalo Feliciano on 25/10/2024.
//

import SwiftUI

struct DemoListaView: View {
    
    @StateObject var vm = DemoListaViewModel()
    
    var body: some View {
        NavigationStack{
            VStack{
                
                HStack{
                    TextField("nome", text: self.$vm.novoNome)
                        .frame(width: 150)
                        .textFieldStyle(.roundedBorder)
                    
                    Button {
                        vm.addPessoa()
                    } label: {
                        Text("Add new")
                            .frame(width: 100, height: 50)
                            .background(.blue)
                            .foregroundStyle(.white)
                            .clipShape(Capsule())
                    }

                    
                }
                .frame(width: 250)
                .padding([.top], 20)
                List(vm.lista){ pessoa in
                    
                    
                    
                    NavigationLink {
                        Text(pessoa.nome)
                        
                    } label: {
                        Text(pessoa.nome)
                        
                    }

                 
                    
                }
                
                
                
            }
        }
    }
}

#Preview {
    DemoListaView()
}
