import streamlit as st
import streamlit.components.v1 as components

# HTML, CSS, and JavaScript code using Three.js with a blue neon tech aesthetic
threejs_neon_html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Three.js Neon Background Animation</title>
  <style>
    /* Ensure the page fills the screen with no scrollbars */
    body, html {
      margin: 0;
      padding: 0;
      overflow: hidden;
      height: 100%;
      /* A fallback background in case Three.js doesn't render immediately */
      background: linear-gradient(45deg, #000428, #004e92);
    }
    /* The canvas covers the full background */
    #bg-canvas {
      position: fixed;
      top: 0;
      left: 0;
      z-index: -1;
      width: 100%;
      height: 100%;
    }
    /* Overlay content styled with neon accents */
    .content {
      position: relative;
      z-index: 1;
      text-align: center;
      color: #00ffff;
      padding-top: 50px;
      font-family: 'Courier New', Courier, monospace;
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
    <h1>Welcome to the Neon Tech App</h1>
    <p>Experience the blue neon vibe with advanced 3D animations!</p>
  </div>

  <!-- Include Three.js library via CDN -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <script>
    // Set up scene, camera, and renderer
    const scene = new THREE.Scene();
    // Set the scene background to a dark blue for contrast
    scene.background = new THREE.Color(0x000428);
    
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({ canvas: document.getElementById("bg-canvas"), antialias: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    
    // Create a rotating wireframe cube with neon blue color
    const geometry = new THREE.BoxGeometry(2, 2, 2);
    const material = new THREE.MeshBasicMaterial({
      color: 0x00ffff,  // Neon blue
      wireframe: true
    });
    const cube = new THREE.Mesh(geometry, material);
    scene.add(cube);
    
    // Position the camera so the cube is visible
    camera.position.z = 5;
    
    // Animation loop to rotate the cube and render the scene
    function animate() {
      requestAnimationFrame(animate);
      cube.rotation.x += 0.01;
      cube.rotation.y += 0.01;
      renderer.render(scene, camera);
    }
    animate();
    
    // Ensure responsiveness on window resize
    window.addEventListener('resize', function() {
      renderer.setSize(window.innerWidth, window.innerHeight);
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
    });
  </script>
</body>
</html>
"""

# Embed the HTML code into the Streamlit app
components.html(threejs_neon_html, height=700)

# Main content of your Streamlit app below the animation
st.write("Your main Streamlit app content goes here.")
