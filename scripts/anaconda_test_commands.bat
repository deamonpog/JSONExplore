REM JSON Scout Testing Commands for Anaconda Prompt
REM Copy and paste these commands one by one

echo "🚀 JSON Scout Package Testing in Anaconda Prompt"

REM Step 1: Ensure you're in the right environment and build
conda activate jsonexplore
python -m build

REM Step 2: Create test environment  
conda create -n jsonanatomy-test python=3.9 -y

REM Step 3: Activate test environment
conda activate jsonanatomy-test

REM Step 4: Install package (adjust path if needed)
pip install dist\json_scout-0.1.0-py3-none-any.whl

REM Step 5: Basic import test
python -c "import jsonanatomy; print('✅ Basic import works')"

REM Step 6: Namespace import test  
python -c "import jsonanatomy as js; print('✅ Namespace import works')"

REM Step 7: Component import test
python -c "from jsonanatomy import Explore, Maybe, Xplore, SimpleXML; print('✅ Component imports work')"

REM Step 8: Basic functionality test
python -c "import jsonanatomy as js; data = {'test': [1, 2, 3]}; explorer = js.Xplore(data); result = explorer['test'][0].value(); print(f'✅ Basic functionality: {result}')"

REM Step 9: Run full test suite
python scripts\test_installation.py

REM Step 10: Cleanup
conda deactivate
conda env remove -n jsonanatomy-test -y
conda activate jsonexplore

echo "✅ Testing complete!"
