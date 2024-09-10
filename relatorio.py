import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import tkinter as tk

def exportar_para_pdf():
    pdf_file = "conteudo_exportado.pdf"
    with PdfPages(pdf_file) as pdf:
        # Renderizar e salvar o gráfico
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Gráfico de Exemplo')
        pdf.savefig(fig)  # Salvar o gráfico no PDF
        plt.close(fig)  # Fechar o gráfico após salvar
    print("PDF exportado com sucesso.")

# Configurar a interface gráfica
root = tk.Tk()
root.title("Exportar para PDF")
botao_exportar = tk.Button(root, text="Exportar Gráfico para PDF", command=exportar_para_pdf)
botao_exportar.pack()

# Iniciar o loop da interface gráfica
root.mainloop()
