//
//  ContentView.swift
//  Listas_vs_mac
//
//  Created by Gonçalo Feliciano on 06/11/2024.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        List {
            Section {
                Text("Ola Mundo")
                Text("Ola Mundo")
                Text("Ola Mundo")
            } header: {
                Text("header Sec 1")
            } footer: {
                Text("footer Sec 1")
            }
            
            Section {
                Text("Ola Mundo")
                Text("Ola Mundo")
                Text("Ola Mundo")
            } header: {
                Text("header Sec 2")
            } footer: {
                Text("footer Sec 2")
            }
        }//List
        
        
    }
}

#Preview {
    ContentView()
}
