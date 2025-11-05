import customtkinter as ctk
import math

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("CALCULADORA DE PAINÉIS")
app.geometry("1500x900")  # largura maior pra caber as 3 colunas

def calcular():
    try:
        for widget in resultado_frame.winfo_children():
            widget.destroy()

        valor1 = float(largura.get())
        valor2 = float(comprimento.get())
        valor3 = float(profundidade.get())

        valor_largura = (valor1 + 2) + (valor3 * 2)
        valor_comprimento = (valor2 + 2) + (valor3 * 2)
        perda_solda = 0.10

        materiais = {
            "PVC TRANÇADO BRANCO/CINZA 0,4MM": {"peso": 0.6, "bobina": 3.0, "preco": 50},
            "PVC PURO PRETO/PRETO 1MM": {"peso": 1.1, "bobina": 2.3, "preco": 68},
            "PVC TRANÇADO AZUL/AZUL 0,9MM": {"peso": 1.3, "bobina": 3.0, "preco": 57},
            "PEAD TRANÇADO VERDE/PRETO 0,75MM": {"peso": 0.45, "bobina": 4.2, "preco": 32},
            "PEAD TRANÇADO PRETO/PRETO 1MM": {"peso": 0.6, "bobina": 4.0, "preco": 40},
        }

        colunas = 3
        linha = 0
        coluna = 0

        for nome, dados in materiais.items():
            peso_especifico = dados["peso"]
            L_bobina = dados["bobina"]
            preco = dados["preco"]

            faixas = math.ceil(valor_largura / (L_bobina - perda_solda))
            largura_real = (faixas * L_bobina) - (perda_solda * (faixas - 1))
            comprimento_real = valor_comprimento
            valor_total_real = largura_real * comprimento_real

            peso_painel = peso_especifico * valor_total_real
            tempo_total_minutos = ((faixas - 1) * 2.5) * valor_comprimento
            horas = int(tempo_total_minutos // 60)
            minutos = int(tempo_total_minutos % 60)
            valor_total = preco * valor_total_real

            # Frame individual de cada material
            bloco = ctk.CTkFrame(resultado_frame, corner_radius=10, border_width=2)
            bloco.grid(row=linha, column=coluna, padx=20, pady=20, sticky="nsew")

            # Título
            ctk.CTkLabel(bloco, text=nome, font=("Arial", 18, "bold"), text_color="#00BFFF").pack(pady=(10, 10))

            # Resultados
            ctk.CTkLabel(bloco, text=f"LARGURA: {largura_real:.2f} m", font=("Arial", 15)).pack(anchor="w", padx=20)
            ctk.CTkLabel(bloco, text=f"COMPRIMENTO: {comprimento_real:.2f} m", font=("Arial", 15)).pack(anchor="w", padx=20)
            ctk.CTkLabel(bloco, text=f"METRAGEM QUADRADA: {valor_total_real:.2f} m²", font=("Arial", 15)).pack(anchor="w", padx=20)
            ctk.CTkLabel(bloco, text=f"PESO DO PAINEL: {peso_painel:.2f} kg", font=("Arial", 15)).pack(anchor="w", padx=20)
            #ctk.CTkLabel(bloco, text=f"TEMPO DE PRODUÇÃO: {horas}h {minutos}min", font=("Arial", 15)).pack(anchor="w", padx=20)
            ctk.CTkLabel(bloco, text=f"VALOR ESTIMADO: R$ {valor_total:.2f}", font=("Arial", 15, "bold")).pack(anchor="w", padx=20, pady=(0, 10))

            # Ajusta posição (3 colunas)
            coluna += 1
            if coluna >= colunas:
                coluna = 0
                linha += 1

    except ValueError:
        for widget in resultado_frame.winfo_children():
            widget.destroy()
        ctk.CTkLabel(
            resultado_frame,
            text="Por favor, digite números válidos (use ponto).",
            font=("Arial", 14, "bold"),
            text_color="red"
        ).grid(row=0, column=0, columnspan=3, pady=20)

# Cabeçalho
frase_label = ctk.CTkLabel(app, text="CALCULADORA DE PAINÉIS DE GEOMEMBRANA", font=("Comic Sans", 14, "bold"))
frase_label.pack(pady=30)

# Entradas lado a lado
entry_frame = ctk.CTkFrame(app)
entry_frame.pack(pady=10)

largura = ctk.CTkEntry(entry_frame, placeholder_text="Largura (m)", width=200, height=40, font=("Arial", 16))
largura.grid(row=0, column=0, padx=10, pady=10)

comprimento = ctk.CTkEntry(entry_frame, placeholder_text="Comprimento (m)", width=200, height=40, font=("Arial", 16))
comprimento.grid(row=0, column=1, padx=10, pady=10)

profundidade = ctk.CTkEntry(entry_frame, placeholder_text="Profundidade (m)", width=200, height=40, font=("Arial", 16))
profundidade.grid(row=0, column=2, padx=10, pady=10)

# Botão
botao = ctk.CTkButton(app, text="Calcular", command=calcular)
botao.pack(pady=20)

# Instrução
instrucao_label = ctk.CTkLabel(app, text="*ATENÇÃO! Utilize ponto (.) ao invés de vírgula (,)", font=("Arial", 14))
instrucao_label.pack(pady=10)

# Resultados organizados em grid (sem scroll)
resultado_frame = ctk.CTkFrame(app)
resultado_frame.pack(pady=20, fill="both", expand=True)

# Rodapé
rodape_label = ctk.CTkLabel(app, text="© 2025 Brasil Piscis   -   Developed by Matheus Tartaglia", font=("Arial", 12))
rodape_label.pack(side="bottom", pady=10)

app.mainloop()
