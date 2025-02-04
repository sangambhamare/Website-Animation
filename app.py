import streamlit as st
import streamlit.components.v1 as components

# HTML, CSS, and JavaScript code using Three.js with multiple moving technical shapes
threejs_shapes_html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Three.js Moving Technical Shapes</title>
  <style>
    /* Fullscreen styling */
    body, html {
      margin: 0;
      padding: 0;
      overflow: hidden;
      height: 100%;
      background: #000428; /* Dark blue background */
    }
    /* The canvas fills the entire window */
    #bg-canvas {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: -1;
    }
    /* Overlay content with neon styling */
    .content {
      position: relative;
      z-index: 1;
      text-align: center;
      color: #00ffff;
      font-family: 'Courier New', Courier, monospace;
      padding-top: 50px;
    }
    .content h1 {
      text-shadow: 0 0 10px #00ffff, 0 0 20px #00ffff;
    }
    .content p {
      text-shadow: 0 0 5px #00ffff;
    }
  </style>
</head>
<body>
  <!-- Canvas for Three.js rendering -->
  <canvas id="bg-canvas"></canvas>
  
  <!-- Overlay content -->
  <div class="content">
    <h1>Neon Tech Shapes</h1>
    <p>Experience moving technical shapes in a futuristic neon style.</p>
  </div>
  
  <!-- Include Three.js via CDN -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <script>
    // Setup scene, camera, and renderer
    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0x000428);

    const camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);
    camera.position.z = 8;

    const renderer = new THREE.WebGLRenderer({ canvas: document.getElementById("bg-canvas"), antialias: true });
    renderer.setSize(window.innerWidth, window.innerHeight);

    // Create an array to hold our shapes
    const shapes = [];
    const neonColor = 0x00ffff; // Neon blue

    // Helper function to create a shape and add it to the scene
    function createShape(geometry, x, y, z) {
      const material = new THREE.MeshBasicMaterial({ color: neonColor, wireframe: true });
      const mesh = new THREE.Mesh(geometry, material);
      mesh.position.set(x, y, z);
      // Store a random rotation speed for each shape
      mesh.userData = { rotationSpeed: Math.random() * 0.02 + 0.01, drift: Math.random() * 0.005 + 0.002 };
      scene.add(mesh);
      shapes.push(mesh);
    }

    // Create multiple shapes with different geometries and random positions
    for (let i = 0; i < 5; i++) {
      // Random positions in a range
      const posX = (Math.random() - 0.5) * 12;
      const posY = (Math.random() - 0.5) * 12;
      const posZ = (Math.random() - 0.5) * 12;
      // Alternate geometries: cube, torus, and sphere
      if (i % 3 === 0) {
        createShape(new THREE.BoxGeometry(2, 2, 2), posX, posY, posZ);
      } else if (i % 3 === 1) {
        createShape(new THREE.TorusGeometry(1.2, 0.4, 16, 100), posX, posY, posZ);
      } else {
        createShape(new THREE.SphereGeometry(1.2, 32, 32), posX, posY, posZ);
      }
    }

    // Animation loop to rotate and move the shapes
    function animate() {
      requestAnimationFrame(animate);

      shapes.forEach(mesh => {
        // Rotate the shape
        mesh.rotation.x += mesh.userData.rotationSpeed;
        mesh.rotation.y += mesh.userData.rotationSpeed;
        // Make the shape drift slowly along the y-axis
        mesh.position.y += mesh.userData.drift;
        // Reverse drift direction if out of bounds
        if (mesh.position.y > 6 || mesh.position.y < -6) {
          mesh.userData.drift = -mesh.userData.drift;
        }
      });

      renderer.render(scene, camera);
    }
    animate();

    // Adjust renderer and camera on window resize
    window.addEventListener('resize', function(){
      renderer.setSize(window.innerWidth, window.innerHeight);
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
    });
  </script>
</body>
</html>
"""

# Embed the HTML code into your Streamlit app
components.html(threejs_shapes_html, height=700)

# Main Streamlit app content below the animation
st.write("Your main Streamlit app content goes here.")
