import customtkinter as ctk
import math

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("CALCULADORA DE PAINEIS")
app.geometry("800x1000")

def calcular():
    try:
        # Recebe os valores digitados
        valor1 = float(largura.get())
        valor2 = float(comprimento.get())
        valor3 = float(profundidade.get())
        
        # Cálculos iniciais com margem extra
        valor_largura = (valor1 + 2) + (valor3 * 2)
        valor_comprimento = (valor2 + 2) + (valor3 * 2)
        

        # Dicionário de pesos
        pesos = {
            "PVC TRANÇADO BRANCO/CINZA 0,4MM": 0.6,
            "PVC PURO PRETO/PRETO 1MM": 1.1,
            "PVC TRANÇADO AZUL/AZUL 0,9MM": 1.3,
            "PEAD TRANÇADO VERDE/PRETO 0,75MM": 0.45,
            "PEAD TRANÇADO PRETO/PRETO 1MM": 0.6,
        }

        # Dicionário de larguras de bobina
        bobinas = {
            "PVC TRANÇADO BRANCO/CINZA 0,4MM": 3.0,
            "PVC PURO PRETO/PRETO 1MM": 2.3,
            "PVC TRANÇADO AZUL/AZUL 0,9MM": 3.0,
            "PEAD TRANÇADO VERDE/PRETO 0,75MM": 4.2,
            "PEAD TRANÇADO PRETO/PRETO 1MM": 4.0,
        }

        perda_solda = 0.10  # 10 cm de perda por solda

        # Material selecionado
        tipo_pvc = menu.get()
        peso_especifico = pesos[tipo_pvc]
        L_bobina = bobinas[tipo_pvc]

        # Ajuste da largura ao múltiplo da bobina
        faixas = math.ceil(valor_largura / (L_bobina - perda_solda))
        largura_real = (faixas * L_bobina) - (perda_solda * (faixas - 1))

        comprimento_real = valor_comprimento  # Comprimento pode ser exato
        valor_total_real = largura_real * comprimento_real

        peso_painel = peso_especifico * valor_total_real
        tempo_solda = ((faixas - 1 ) * 2.5) * valor_comprimento 
        tempo_real = tempo_solda / 60

        # Converte tempo de solda para horas e minutos
        tempo_total_minutos = ((faixas - 1) * 2.5) * valor_comprimento  # já em minutos
        horas = int(tempo_total_minutos // 60)  # parte inteira = horas
        minutos = int(tempo_total_minutos % 60) # resto = minutos

        

        # Atualiza os resultados
        resposta_label.configure(text=f"LARGURA: {largura_real:.2f} m")
        resposta_label1.configure(text=f"COMPRIMENTO: {comprimento_real:.2f} m")
        resposta_label2.configure(text=f"METRAGEM QUADRADA (M²): {valor_total_real:.2f} m²")
        resposta_label3.configure(text=f"PESO DO PAINEL: {peso_painel:.2f} kg")
        resposta_label4.configure(text=f"TEMPO DE SOLDA APROX: {horas}h {minutos}min")

    except ValueError:
        resposta_label.configure(text="Por favor, digite um número válido (use ponto).")
        resposta_label1.configure(text="")
        resposta_label2.configure(text="")
        resposta_label3.configure(text="")
    except Exception as e:
        resposta_label.configure(text="Erro inesperado — veja o console.")
        resposta_label1.configure(text=str(e))
        resposta_label2.configure(text="")
        resposta_label3.configure(text="")
        print("Exception in calcular():", repr(e))

# Cabeçalho
frase_label = ctk.CTkLabel(app, text="CALCULADORA DE PAINEIS DE GEOMEMBRANA", font=("Comic Sans", 14, "bold"))
frase_label.pack(pady=30, padx=40)

# Entry para largura
largura = ctk.CTkEntry(app, placeholder_text="Digite a largura (em metros)", width=310, height=40, font=("Arial", 16))
largura.pack(pady=20)

# Entry para comprimento
comprimento = ctk.CTkEntry(app, placeholder_text="Digite o comprimento (em metros)", width=310, height=40, font=("Arial", 16))
comprimento.pack(pady=20)

# Entry para profundidade
profundidade = ctk.CTkEntry(app, placeholder_text="Digite a profundidade (em metros)", width=310, height=40, font=("Arial", 16))
profundidade.pack(pady=20)

# Menu de seleção de material
menu = ctk.CTkOptionMenu(
    app,
    values=[
        "PVC TRANÇADO BRANCO/CINZA 0,4MM",
        "PVC PURO PRETO/PRETO 1MM",
        "PVC TRANÇADO AZUL/AZUL 0,9MM",
        "PEAD TRANÇADO VERDE/PRETO 0,75MM",
        "PEAD TRANÇADO PRETO/PRETO 1MM"
    ],
    command=lambda _: calcular()
)
menu.pack(pady=20)
menu.set("PVC PURO PRETO/PRETO 1MM")

# Botão de calcular
botao = ctk.CTkButton(app, text="Calcular", command=calcular)
botao.pack(pady=10)

# Frase de instrução
instrucao_label = ctk.CTkLabel(app, text="*ATENÇÃO! Utilize ponto (.) ao invés de vírgula (,)", font=("Arial", 14))
instrucao_label.pack(pady=10)

# Área de respostas
resultado_frame = ctk.CTkFrame(app)
resultado_frame.pack(pady=20)

# Coluna 1
resposta_label  = ctk.CTkLabel(resultado_frame, text="", font=("Arial", 16))
resposta_label1 = ctk.CTkLabel(resultado_frame, text="", font=("Arial", 16))
resposta_label2 = ctk.CTkLabel(resultado_frame, text="", font=("Arial", 16))
resposta_label3 = ctk.CTkLabel(resultado_frame, text="", font=("Arial", 16))
resposta_label4 = ctk.CTkLabel(resultado_frame, text="", font=("Arial", 16))

resposta_label.grid(row=0, column=0, padx=20, pady=5, sticky="w")
resposta_label1.grid(row=1, column=0, padx=20, pady=5, sticky="w")
resposta_label2.grid(row=2, column=0, padx=20, pady=5, sticky="w")
resposta_label3.grid(row=3, column=0, padx=20, pady=5, sticky="w")
resposta_label4.grid(row=3, column=0, padx=20, pady=5, sticky="w")

# Rodapé
rodape_label = ctk.CTkLabel(app, text="© 2025 Brasil Piscis   -   Developed by Matheus Tartalha", font=("Arial", 12))
rodape_label.pack(side="bottom", pady=10)

app.mainloop()


# preco pvc 0.9 68,00
# preco pead 0-75 32,00
# preco pvc trancado 57,00
# pvc cinza 50,00
# pead 1mm 40,00