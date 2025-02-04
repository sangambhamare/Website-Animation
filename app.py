import streamlit as st
import streamlit.components.v1 as components

advanced_threejs_html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Advanced Neon Tech Shapes with Bloom</title>
  <style>
    /* Fullscreen setup */
    body, html {
      margin: 0;
      padding: 0;
      overflow: hidden;
      height: 100%;
      background: #000428; /* Dark blue backdrop */
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
    <h1>Advanced Neon Tech Shapes</h1>
    <p>Enjoy advanced animations with glowing bloom effects!</p>
  </div>
  
  <!-- Include Three.js library -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <!-- Include EffectComposer and bloom passes for postprocessing -->
  <script src="https://unpkg.com/three@0.128.0/examples/js/postprocessing/EffectComposer.js"></script>
  <script src="https://unpkg.com/three@0.128.0/examples/js/postprocessing/RenderPass.js"></script>
  <script src="https://unpkg.com/three@0.128.0/examples/js/postprocessing/UnrealBloomPass.js"></script>
  
  <script>
    let scene, camera, renderer, composer, bloomPass;
    let shapes = [];
    const neonColor = new THREE.Color(0x00ffff); // Neon blue color

    // Parameters for bloom effect
    const params = {
      exposure: 1,
      bloomStrength: 1.5,
      bloomThreshold: 0,
      bloomRadius: 0
    };

    function init() {
      // Create scene and camera
      scene = new THREE.Scene();
      scene.background = new THREE.Color(0x000428); // Dark blue background
      
      camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
      camera.position.z = 10;

      // Setup renderer
      renderer = new THREE.WebGLRenderer({ canvas: document.getElementById("bg-canvas"), antialias: true });
      renderer.setSize(window.innerWidth, window.innerHeight);
      renderer.toneMappingExposure = Math.pow(params.exposure, 4.0);

      // Set up postprocessing (composer with bloom)
      composer = new THREE.EffectComposer(renderer);
      const renderScene = new THREE.RenderPass(scene, camera);
      composer.addPass(renderScene);
      
      bloomPass = new THREE.UnrealBloomPass(
        new THREE.Vector2(window.innerWidth, window.innerHeight),
        params.bloomStrength,
        params.bloomRadius,
        params.bloomThreshold
      );
      composer.addPass(bloomPass);

      // Create multiple advanced shapes
      for (let i = 0; i < 15; i++) {
        let geometry;
        // Randomly choose a geometry: cube, torus, or sphere
        const rand = Math.random();
        if (rand < 0.33) {
          geometry = new THREE.BoxGeometry(1.5, 1.5, 1.5);
        } else if (rand < 0.66) {
          geometry = new THREE.TorusGeometry(0.8, 0.3, 16, 100);
        } else {
          geometry = new THREE.SphereGeometry(0.8, 32, 32);
        }
        const material = new THREE.MeshBasicMaterial({ color: neonColor, wireframe: true });
        const mesh = new THREE.Mesh(geometry, material);
        // Set random initial position within a range
        mesh.position.set((Math.random()-0.5)*20, (Math.random()-0.5)*20, (Math.random()-0.5)*20);
        // Assign random rotation speeds and drift directions
        mesh.userData = {
          rotationSpeedX: (Math.random()-0.5)*0.05,
          rotationSpeedY: (Math.random()-0.5)*0.05,
          driftX: (Math.random()-0.5)*0.02,
          driftY: (Math.random()-0.5)*0.02,
          driftZ: (Math.random()-0.5)*0.02
        };
        scene.add(mesh);
        shapes.push(mesh);
      }
    }

    function animate() {
      requestAnimationFrame(animate);
      
      // Update shapes rotation and position
      shapes.forEach(mesh => {
        mesh.rotation.x += mesh.userData.rotationSpeedX;
        mesh.rotation.y += mesh.userData.rotationSpeedY;
        mesh.position.x += mesh.userData.driftX;
        mesh.position.y += mesh.userData.driftY;
        mesh.position.z += mesh.userData.driftZ;
        // Wrap around if a shape moves too far from the center
        if (mesh.position.x > 10) mesh.position.x = -10;
        if (mesh.position.x < -10) mesh.position.x = 10;
        if (mesh.position.y > 10) mesh.position.y = -10;
        if (mesh.position.y < -10) mesh.position.y = 10;
        if (mesh.position.z > 10) mesh.position.z = -10;
        if (mesh.position.z < -10) mesh.position.z = 10;
      });
      
      // Render the scene using composer to include bloom effect
      composer.render();
    }

    // Adjust camera and renderer on window resize for responsiveness
    window.addEventListener('resize', function(){
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(window.innerWidth, window.innerHeight);
      composer.setSize(window.innerWidth, window.innerHeight);
    });

    init();
    animate();
  </script>
</body>
</html>
"""

# Embed the advanced HTML code into the Streamlit app
components.html(advanced_threejs_html, height=700)

# Additional main content for your Streamlit app
st.write("Main Streamlit app content goes here.")
