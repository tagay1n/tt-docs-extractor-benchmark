import yaml
import itertools
from runners.gemini_pdf_runner import run_pdf
# from runners.gemini_image_runner import run_images

def run():
    for s in generate_scenarios():
        print(f"Running scenario: {s}")
        if s["input_types"] == "pdf":
            run_pdf(s)
        else:
            pass
            # run_images(s)
            
def generate_scenarios(config_path="config/scenarios.yml"):
    with open(config_path) as f:
        config = yaml.safe_load(f)

    keys, values = zip(*config['gemini'].items())
    combinations = [dict(zip(keys, v)) for v in itertools.product(*values)]

    # for combo in combinations:
    #     combo["id"] = (
    #         f"{combo['model']}_{combo['input_types']}_"
    #         f"{combo['shots']}shot_{'sys' if combo['system_prompts'] else 'nosys'}_"
    #         f"b{combo['batch_sizes']}"
    #     )
    return combinations    
            

if __name__ == "__main__":
    run()


