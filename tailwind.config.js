tailwind.config = {
    theme: {
        extend: {
            colors: {
                'halo-void': '#050b14',     /* Azul espacio profundo */
                'halo-ring': '#4361ee',     /* Azul metálico estructura */
                'halo-energy': '#4cc9f0',   /* Cyan brillante plasma */
                'halo-text': '#f8fafc',     /* Blanco estelar */
                'halo-accent': '#1e40af',   /* Azul oscuro militar */
                'halo-success': '#10b981'   /* Verde confirmación */
            },
            fontFamily: {
                'sans': ['Inter', 'sans-serif'],
                'display': ['Space Grotesk', 'sans-serif'],
                'mono': ['Space Mono', 'monospace'],
            },
            backgroundImage: {
                'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
            }
        }
    }
}
