import re

html_file = r'c:\Users\Human\Downloads\CumpleHeber\index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

slides_data = [
    (6, 'Registro Estelar', 'Trayectoria Brillante', 'M13 10V3L4 14h7v7l9-11h-7z'),
    (1, 'Exploración Base', 'Nuevos Horizontes', 'M12 19l9 2-9-18-9 18 9-2zm0 0v-8'),
    (2, 'Archivo Personal', 'Un recuerdo imborrable', 'M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 111.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z'),
    (3, 'Comando Central UNSC', 'Unidos en cualquier galaxia', 'M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z'),
    (4, 'Base de Operaciones', 'Misión Cumplida', 'M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z'),
    (5, 'Archivo Confidencial', 'Memoria Recuperada', 'M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z'),
    (6, 'Registro Estelar', 'Trayectoria Brillante', 'M13 10V3L4 14h7v7l9-11h-7z'),
    (1, 'Exploración Base', 'Nuevos Horizontes', 'M12 19l9 2-9-18-9 18 9-2zm0 0v-8')
]

html_slides = \"\\n\"
for i, data in enumerate(slides_data):
    num, title1, title2, path = data
    slide_comment = f'<!-- Slide {num} -->'
    if i == 0:
        slide_comment = f'<!-- Slide {num} (Clonado al inicio) -->'
    elif i == len(slides_data) - 1:
        slide_comment = f'<!-- Slide {num} (Clonado al final) -->'
        
    html_slides += f'''                        {slide_comment}
                        <div class="w-full h-full shrink-0 relative flex justify-center items-center">
                            <img src="S{num}.jpg" 
                                 alt="{title1}" 
                                 class="w-full h-full object-cover opacity-100 hover:scale-105 transition-all duration-700 ease-in-out scanlines">
                            <div class="absolute inset-0 bg-gradient-to-t from-halo-void via-halo-void/30 to-transparent pointer-events-none"></div>
                            <div class="absolute bottom-6 left-6 md:bottom-10 md:left-10 z-10 pointer-events-none">
                                <p class="text-halo-energy font-mono tracking-widest uppercase text-xs md:text-sm mb-2 flex items-center gap-2 drop-shadow-md">
                                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="{path}"></path></svg>
                                    {title1}
                                </p>
                                <h3 class="text-2xl md:text-4xl font-display text-white font-bold drop-shadow-lg uppercase">{title2}</h3>
                            </div>
                        </div>\\n\\n'''

new_content = re.sub(r'(<div id="banner-slider"[^>]*>).*?(?=                    </div>\\n                    <!-- Flecha Derecha -->)', r'\\1' + html_slides, content, flags=re.DOTALL)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(new_content)
print('Slider updated.')
