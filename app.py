import streamlit as st
import streamlit.components.v1 as components

# HTML, CSS, and JavaScript code using Three.js for an advanced 3D animation background
threejs_html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Three.js Background Animation</title>
  <style>
    /* Make sure body and html take up full height with no margins */
    body, html {
      margin: 0;
      padding: 0;
      overflow: hidden;
      height: 100%;
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
    /* Content styling to ensure it appears above the animation */
    .content {
      position: relative;
      z-index: 1;
      text-align: center;
      color: white;
      padding-top: 50px;
      font-family: sans-serif;
    }
  </style>
</head>
<body>
  <!-- Canvas for Three.js rendering -->
  <canvas id="bg-canvas"></canvas>
  
  <!-- Overlay content -->
  <div class="content">
    <h1>Welcome to My Advanced Animated App</h1>
    <p>Enjoy the immersive Three.js 3D background animation!</p>
  </div>

  <!-- Include Three.js library via CDN -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <script>
    // Set up scene, camera, and renderer
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({ canvas: document.getElementById("bg-canvas"), antialias: true });
    renderer.setSize(window.innerWidth, window.innerHeight);

    // Create a rotating wireframe cube
    const geometry = new THREE.BoxGeometry(2, 2, 2);
    const material = new THREE.MeshBasicMaterial({ color: 0x44aa88, wireframe: true });
    const cube = new THREE.Mesh(geometry, material);
    scene.add(cube);

    // Position the camera so that the cube is visible
    camera.position.z = 5;

    // Animation loop to rotate the cube and render the scene
    function animate() {
      requestAnimationFrame(animate);
      cube.rotation.x += 0.01;
      cube.rotation.y += 0.01;
      renderer.render(scene, camera);
    }
    animate();

    // Adjust canvas size and camera on window resize for responsiveness
    window.addEventListener('resize', function(){
      renderer.setSize(window.innerWidth, window.innerHeight);
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
    });
  </script>
</body>
</html>
"""

# Embed the HTML code into the Streamlit app
components.html(threejs_html, height=700)

# Main content of your Streamlit app
st.write("Your main Streamlit app content goes here.")
