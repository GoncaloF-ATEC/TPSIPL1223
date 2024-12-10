//
//  LoadData.swift
//  LoadApi
//
//  Created by Gonçalo Feliciano on 08/11/2024.
//

import Foundation


class LoadData: ObservableObject{
    
    var url:URL
    
    init(url: String) {
        self.url = URL(string: url)!
    }
    
    
    func loadAllData(complition: @escaping (ToDos) -> () ){
        
        
        var urlReq = URLRequest(url: self.url)
        urlReq.httpMethod = "PoSt"

        //urlReq.setValue("key", forHTTPHeaderField: "dasdkshfiusfhsdfj")
        
        
        let dataTask = URLSession.shared.dataTask(with: urlReq) { dados, resp, erro in
            
            // lidar com erro
            if let erro = erro{
                print("Erro \(erro.localizedDescription)")
                return
            }
            
            // validar resp
            guard let resp = resp as? HTTPURLResponse, (200...299).contains(resp.statusCode) else{
                
                print("Erro no codigo de resposta: \((resp as! HTTPURLResponse).statusCode)")
                return
            }

            // decode dos dados
            if let dados = dados, let myData = try? JSONDecoder().decode(ToDos.self, from: dados) {
                
                complition(myData)
            }
        }//  URLSession.shared.dataTask
        dataTask.resume()
    }
       
       
    

}
