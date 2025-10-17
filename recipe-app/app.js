const express = require('express');
const path = require('path');
const app = express();
const PORT = process.env.PORT || 3000;

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')));

// In-memory recipes store (example)
let recipes = [
    { id: 1, title: '和風だしの味噌汁', description: '基本の味噌汁。豆腐とわかめでシンプルに。', ingredients: ['水', 'だし', '味噌', '豆腐', 'わかめ'], steps: ['だしをとる', '具材を煮る', '味噌を溶かす'] },
    { id: 2, title: '基本のオムレツ', description: 'ふわふわオムレツの作り方', ingredients: ['卵', 'バター', '塩', 'こしょう'], steps: ['卵を溶く', 'フライパンで焼く', '巻く'] },
    { id: 3, title: '照り焼きチキン', description: 'ごはんに合う定番のおかず。甘辛ダレで照りよく焼き上げます。', ingredients: ['鶏もも肉', '醤油', 'みりん', '砂糖', '酒', '生姜', 'サラダ油'], steps: ['鶏肉に下味（醤油・酒・生姜）をつける', 'フライパンで皮目をこんがり焼く', '余分な油を拭き取りタレ（醤油・みりん・砂糖）を加える', 'タレを煮詰めて照りを出し、切って盛り付ける'] }
];

app.get('/', (req, res) => {
    res.render('index', { recipes });
});

app.get('/recipes/new', (req, res) => {
    res.render('new');
});

app.post('/recipes', (req, res) => {
    const { title, description, ingredients, steps } = req.body;
    const id = recipes.length ? recipes[recipes.length - 1].id + 1 : 1;
    const newRecipe = {
        id,
        title: title || 'Untitled',
        description: description || '',
        ingredients: ingredients ? ingredients.split('\n').map(s => s.trim()).filter(Boolean) : [],
        steps: steps ? steps.split('\n').map(s => s.trim()).filter(Boolean) : []
    };
    recipes.push(newRecipe);
    res.redirect(`/recipes/${id}`);
});

app.get('/recipes/:id', (req, res) => {
    const id = Number(req.params.id);
    const recipe = recipes.find(r => r.id === id);
    if (!recipe) return res.status(404).send('Recipe not found');
    res.render('show', { recipe });
});

app.listen(PORT, () => {
    console.log(`Recipe app running on http://localhost:${PORT}`);
});
