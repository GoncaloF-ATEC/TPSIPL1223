//
//  ContentView.swift
//  LoadApi
//
//  Created by Gonçalo Feliciano on 08/11/2024.
//

import SwiftUI

struct ContentView: View {
    
    
    @StateObject var laodData = LoadData(url: "https://jsonplaceholder.typicode.com/todos")
    
    @State var lista:ToDos = []
    
    
    var body: some View {
        VStack {
         
            List {
                ForEach(lista) { todo in
                    Text(todo.title)
                }
     
            }
            Button {
                self.laodData.loadAllData { todos in
                    lista.append(contentsOf: todos)
                }
            } label: {
                Text("LoadData")
            }


        }
        .onAppear {
           
        }
    
        .padding()
    }
}

#Preview {
    ContentView()
}
