import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */
const sidebars: SidebarsConfig = {
  // By default, Docusaurus generates a sidebar from the docs folder structure
  tutorialSidebar: [
    'intro',
    {
      type: 'category',
      label: 'Module 1: The Robotic Nervous System (ROS 2)',
      items: [
        'module-1-ros2/chapter-1-nervous-system',
        'module-1-ros2/chapter-2-ros-communication',
        'module-1-ros2/chapter-3-digital-brain-to-body'
      ],
    },
    {
      type: 'category',
      label: 'Module 2: The Digital Twin',
      items: [
        'module-2-digital-twin/module-2-chapter-1',
        'module-2-digital-twin/module-2-chapter-2',
        'module-2-digital-twin/module-2-chapter-3'
      ],
    },
    {
      type: 'category',
      label: 'Module 3: The AI-Robot Brain',
      items: [
        'module-3-ai-robot-brain/module-3-chapter-1',
        'module-3-ai-robot-brain/module-3-chapter-2',
        'module-3-ai-robot-brain/module-3-chapter-3'
      ],
    },
    {
      type: 'category',
      label: 'Module 4: Vision-Language-Action',
      items: [
        'module-4-vision-language-action/module-4-chapter-1',
        'module-4-vision-language-action/module-4-chapter-2',
        'module-4-vision-language-action/module-4-chapter-3'
      ],
    },
  ],

  // But you can create a sidebar manually
  /*
  tutorialSidebar: [
    'intro',
    'hello',
    {
      type: 'category',
      label: 'Tutorial',
      items: ['tutorial-basics/create-a-document'],
    },
  ],
   */
};

export default sidebars;
