#!/usr/bin/env node
/**
 * Java First-Principles Tutor CLI
 * Cross-agent learning companion and state manager.
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const ROOT_DIR = __dirname;
const PROGRESS_PATH = path.join(ROOT_DIR, 'progress.json');
const ROADMAP_PATH = path.join(ROOT_DIR, 'curriculum', 'roadmap.json');
const PROGRESS_MD_PATH = path.join(ROOT_DIR, 'PROGRESS.md');

function loadJSON(filepath) {
  try {
    return JSON.parse(fs.readFileSync(filepath, 'utf8'));
  } catch (err) {
    console.error(`Error loading JSON from ${filepath}:`, err.message);
    process.exit(1);
  }
}

function saveJSON(filepath, data) {
  fs.writeFileSync(filepath, JSON.stringify(data, null, 2), 'utf8');
}

function getRoadmap() {
  return loadJSON(ROADMAP_PATH);
}

function getProgress() {
  return loadJSON(PROGRESS_PATH);
}

function getAllLessons(roadmap) {
  const list = [];
  for (const phase of roadmap.phases) {
    for (const lesson of phase.lessons) {
      list.push({
        ...lesson,
        phase_id: phase.id,
        phase_name: phase.name
      });
    }
  }
  return list;
}

function generateProgressMarkdown(progress, roadmap) {
  const allLessons = getAllLessons(roadmap);
  const total = allLessons.length;
  const completedCount = progress.completed_lessons.length;
  const percent = total > 0 ? ((completedCount / total) * 100).toFixed(1) : 0;

  const barLength = 25;
  const filled = Math.round((completedCount / total) * barLength);
  const empty = barLength - filled;
  const progressBar = '█'.repeat(filled) + '░'.repeat(empty);

  let md = `# 🎓 CSE Java Systems & First-Principles Dashboard\n\n`;
  md += `> **Learner:** ${progress.student.title}\n`;
  md += `> **Methodology:** ${progress.student.learning_style}\n`;
  md += `> **Last Active:** ${new Date().toISOString().split('T')[0]}\n\n`;

  md += `## 📊 Progress Overview\n\n`;
  md += `\`\`\`text\n`;
  md += `Progress: [${progressBar}] ${percent}% (${completedCount}/${total} Lessons)\n`;
  md += `Exercises Passed: ${progress.stats.exercises_passed || 0}\n`;
  md += `\`\`\`\n\n`;

  md += `## 📍 Current Station\n\n`;
  md += `- **Phase:** \`${progress.current_position.phase_name}\`\n`;
  md += `- **Current Lesson:** \`${progress.current_position.lesson_id}\` - **${progress.current_position.lesson_title}**\n`;
  md += `- **Status:** \`${progress.current_position.status}\`\n\n`;

  md += `### 💡 How to Continue with Any AI Agent\n`;
  md += `Simply prompt your AI (Antigravity, Claude Code, OpenCode, Gemini CLI):\n`;
  md += `> *"I am ready for my next lesson. Let's study."* or *"Let's practice the current exercise."*\n\n`;

  md += `## 🗺️ Master Curriculum Roadmap\n\n`;

  for (const phase of roadmap.phases) {
    md += `### ${phase.name}\n`;
    md += `*${phase.summary}*\n\n`;
    md += `| Status | ID | Lesson Title | Hardware & Systems Focus |\n`;
    md += `| :---: | :---: | :--- | :--- |\n`;

    for (const lesson of phase.lessons) {
      const isCompleted = progress.completed_lessons.some(c => c.id === lesson.id);
      const isCurrent = progress.current_position.lesson_id === lesson.id;
      let statusIcon = '⬜ Not Started';
      if (isCompleted) {
        statusIcon = '✅ Completed';
      } else if (isCurrent) {
        statusIcon = '🔄 **IN PROGRESS**';
      }

      md += `| ${statusIcon} | \`${lesson.id}\` | [${lesson.title}](lessons/${lesson.id.toLowerCase()}.md) | ${lesson.hardware_focus} |\n`;
    }
    md += `\n`;
  }

  if (progress.completed_lessons.length > 0) {
    md += `## 🏆 Completed Lessons Log\n\n`;
    md += `| Date | ID | Title | Key Takeaway |\n`;
    md += `| :--- | :---: | :--- | :--- |\n`;
    for (const c of progress.completed_lessons) {
      md += `| ${c.completed_at || 'Recently'} | \`${c.id}\` | ${c.title} | ${c.key_takeaway || 'Mastered first principles'} |\n`;
    }
    md += `\n`;
  }

  if (progress.concepts_mastered && progress.concepts_mastered.length > 0) {
    md += `## 🧠 Concepts Mastered\n\n`;
    for (const concept of progress.concepts_mastered) {
      md += `- ✓ **${concept.name}**: ${concept.summary}\n`;
    }
    md += `\n`;
  }

  return md;
}

function sync() {
  const roadmap = getRoadmap();
  const progress = getProgress();
  const allLessons = getAllLessons(roadmap);
  
  progress.stats.total_lessons = allLessons.length;
  progress.stats.completed_lessons_count = progress.completed_lessons.length;
  progress.stats.overall_progress_percent = parseFloat(
    ((progress.completed_lessons.length / allLessons.length) * 100).toFixed(1)
  );
  progress.student.last_active = new Date().toISOString().split('T')[0];

  saveJSON(PROGRESS_PATH, progress);
  const md = generateProgressMarkdown(progress, roadmap);
  fs.writeFileSync(PROGRESS_MD_PATH, md, 'utf8');
  console.log('✅ Synchronized progress.json and PROGRESS.md successfully!');
}

function printStatus() {
  sync();
  const progress = getProgress();
  const roadmap = getRoadmap();
  const allLessons = getAllLessons(roadmap);

  const completed = progress.completed_lessons.length;
  const total = allLessons.length;
  const pct = ((completed / total) * 100).toFixed(1);

  console.log('\n======================================================');
  console.log('  🚀 CSE FIRST-PRINCIPLES JAVA & SYSTEMS TUTOR');
  console.log('======================================================');
  console.log(`👤 Student:     ${progress.student.title}`);
  console.log(`📈 Progress:    ${completed}/${total} lessons completed (${pct}%)`);
  console.log(`🎯 Current:     [${progress.current_position.lesson_id}] ${progress.current_position.lesson_title}`);
  console.log(`🏛️  Phase:       ${progress.current_position.phase_name}`);
  console.log(`⚡ Status:      ${progress.current_position.status}`);
  console.log('------------------------------------------------------');
  console.log('💡 Quick Commands:');
  console.log('   node tutor next           -> Show upcoming lesson details');
  console.log('   node tutor complete <ID>  -> Mark a lesson as mastered');
  console.log('   node tutor roadmap        -> View the complete syllabus');
  console.log('======================================================\n');
}

function showNext() {
  const progress = getProgress();
  const roadmap = getRoadmap();
  const allLessons = getAllLessons(roadmap);

  const currentId = progress.current_position.lesson_id;
  const currentLesson = allLessons.find(l => l.id === currentId);

  if (!currentLesson) {
    console.log('🎉 Congratulations! You have completed all lessons in the curriculum!');
    return;
  }

  console.log('\n======================================================');
  console.log(`📖 ACTIVE LESSON: [${currentLesson.id}] ${currentLesson.title}`);
  console.log(`📁 Phase: ${currentLesson.phase_name}`);
  console.log('======================================================');
  console.log('🎯 Learning Objectives:');
  currentLesson.objectives.forEach((obj, idx) => {
    console.log(`   ${idx + 1}. ${obj}`);
  });
  console.log('\n⚡ Hardware & Systems Connection:');
  console.log(`   ${currentLesson.hardware_focus}`);
  console.log('\n⏱️  Estimated Time: ' + currentLesson.estimated_hours + ' hours');
  console.log('------------------------------------------------------');
  console.log('💬 Ask your AI Agent:');
  console.log(`   "Teach me lesson ${currentLesson.id}: ${currentLesson.title} with deep visual diagrams."`);
  console.log('======================================================\n');
}

function markComplete(lessonId, takeaway = 'Mastered first principles and hardware connection.') {
  const roadmap = getRoadmap();
  const progress = getProgress();
  const allLessons = getAllLessons(roadmap);

  const lessonIndex = allLessons.findIndex(l => l.id.toLowerCase() === (lessonId || '').toLowerCase());
  if (lessonIndex === -1) {
    console.error(`❌ Lesson '${lessonId}' not found in curriculum.`);
    return;
  }

  const targetLesson = allLessons[lessonIndex];

  // Add to completed if not already there
  const alreadyCompleted = progress.completed_lessons.find(c => c.id === targetLesson.id);
  if (!alreadyCompleted) {
    progress.completed_lessons.push({
      id: targetLesson.id,
      title: targetLesson.title,
      phase_id: targetLesson.phase_id,
      completed_at: new Date().toISOString().split('T')[0],
      key_takeaway: takeaway
    });
  }

  // Advance to next lesson
  if (lessonIndex + 1 < allLessons.length) {
    const nextLesson = allLessons[lessonIndex + 1];
    progress.current_position = {
      phase_id: nextLesson.phase_id,
      phase_name: nextLesson.phase_name,
      lesson_id: nextLesson.id,
      lesson_title: nextLesson.title,
      status: 'ready_to_start',
      active_exercise_id: null
    };
  } else {
    progress.current_position.status = 'all_completed';
  }

  saveJSON(PROGRESS_PATH, progress);
  sync();
  console.log(`🎉 Lesson ${targetLesson.id} marked as COMPLETED!`);
  if (progress.current_position.status !== 'all_completed') {
    console.log(`➡️  Next up: [${progress.current_position.lesson_id}] ${progress.current_position.lesson_title}`);
  }
}

function showRoadmap() {
  const roadmap = getRoadmap();
  const progress = getProgress();

  console.log('\n🗺️  FULL MASTER CURRICULUM ROADMAP:');
  for (const phase of roadmap.phases) {
    console.log(`\n📌 ${phase.name}`);
    console.log(`   ${phase.summary}`);
    for (const l of phase.lessons) {
      const isDone = progress.completed_lessons.some(c => c.id === l.id);
      const isCurr = progress.current_position.lesson_id === l.id;
      const icon = isDone ? '✅' : isCurr ? '👉' : '⚪';
      console.log(`   ${icon} [${l.id}] ${l.title}`);
    }
  }
  console.log('\n');
}

// Command dispatcher
const args = process.argv.slice(2);
const command = args[0] ? args[0].toLowerCase() : 'status';

switch (command) {
  case 'status':
    printStatus();
    break;
  case 'sync':
    sync();
    break;
  case 'next':
    showNext();
    break;
  case 'complete':
    markComplete(args[1], args.slice(2).join(' '));
    break;
  case 'roadmap':
    showRoadmap();
    break;
  default:
    console.log(`Unknown command: ${command}`);
    console.log('Available commands: status, next, complete <id> [notes], roadmap, sync');
}
