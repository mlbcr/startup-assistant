def format_prompt(msg: str) -> str:
    data = '''
  Meu nome é Maria Luísa, sou estudante de Ciência da Computação no CEFET/RJ e estou desenvolvendo um projeto que quero transformar em uma startup com impacto social voltado à educação inclusiva. 
  Minha ideia se chama Mnemoro — um aplicativo gamificado que utiliza técnicas mnemônicas (como o Palácio da Memória, repetição espaçada e visualizações criativas) para ajudar crianças com TDAH 
  a melhorar a memória, a concentração e a organização do pensamento, além de ganhar confiança. A proposta é criar um ambiente visual e divertido, com desafios diários e recompensas, que incentive o uso das técnicas de memorização adaptadas para o perfil cognitivo das crianças com TDAH.

 Ainda não tenho um protótipo, mas estou desenvolvendo o conceito, o fluxo de uso e estou estudando como essas técnicas podem ser aplicadas de forma lúdica. Estou começando do zero e busco apoio para estruturar o MVP e validar a solução com usuários reais (crianças, pais e professores).
 Não sei nada sobre negócios ou termos técnicos. 
 Quero me inscrever no Edital FAPERJ HUB RJ STARTUP 2025 (Edital nº 04/2025). Ele é dividido em três fases:

Fase 1 (PAFE) – 12 semanas, com mentorias para estruturar o negócio e validar a ideia.

Fase 2 – 20 semanas, com R$ 30 mil de fomento para construir o protótipo e testar com usuários.

Fase 3 – 32 semanas, com R$ 50 mil para desenvolver o MVP e apresentar no DemoDay.

As inscrições foram abertas em março e vão até 29 de abril de 2025. O foco do edital é inovação digital com impacto social no Estado do Rio de Janeiro, incluindo áreas como educação, saúde e inclusão — o que se alinha perfeitamente ao Mnemoro.
  '''

    context = '''
  # O que são Startups?
  Em resumo, startup é um modelo de negócio inovador, repetível e escalável, e, exatamente por apresentar uma inovação ao mercado, esse negócio gera muitas incertezas, sobretudo no começo.
  # Recursos essenciais para startups:
  - Recursos Humanos:
  No início, a equipe deve ser composta por pessoas com diferentes competências: especialistas em negócios, tecnologia, administração e vendas.
  Mentores são fundamentais, pois trazem expertise e networking, ajudando a acelerar o crescimento da startup.
  - Recursos Técnicos:
  A prototipagem é necessária para validar o produto com o cliente. O feedback da validação é usado para ajustes ou pivotagem (mudança de direção do modelo de negócios).
  Validar o protótipo é uma etapa crítica para garantir que o produto atende às necessidades do mercado.
  - Recursos Financeiros:
  O financiamento vem de várias fontes, dependendo do estágio da startup. Recursos próprios, familiares (love money), investidores-anjo, venture capital, crowdfunding e financiamento público são algumas das opções.
  Investidores buscam startups com um produto mínimo viável (MVP) funcional, para maximizar as chances de sucesso com o capital investido.
  # Estágios de desenvolvimento (T0 a T4):
  - T0 – Curiosidade:
  O empreendedor ainda está pesquisando sobre startups e entendendo o mercado. Ele busca informações e ideias para desenvolver um negócio inovador.
  - T1 – Ideação:
  O projeto está em fase de concepção. O empreendedor já tem uma ideia clara e começa a desenhar o modelo de negócios, definir o público-alvo e testar o protótipo (MVP) com clientes reais.
  - T2 – Operação:
  A startup já validou seu modelo de negócios, tem clientes e começou a gerar receita. Nesta fase, o foco é ganhar tração e buscar mais investimentos para crescer.
  - T3 – Tração:
  A startup busca aumentar sua escala de operações. O objetivo é crescer rapidamente, muitas vezes com a ajuda de novos investidores ou parceiros estratégicos.
  - T4 – Estrela:
  A startup já é lucrativa e está estabelecida no mercado, com alto faturamento e uma base sólida de clientes. Empresas nesse estágio geralmente buscam expandir internacionalmente ou diversificar seus produtos.
  # Tipos de investimento disponíveis:
  - Love Money ou Pai-trocínio:
  Investimento inicial que vem de familiares ou amigos, sem grandes exigências de garantias.
  - Crowdfunding:
  Financiamento coletivo que capta recursos por meio de plataformas online. Ideal para projetos de impacto social ou produtos inovadores.
  - Investidor-Anjo:
  Pessoas físicas que investem em startups de alto risco. Eles também oferecem orientação e networking para ajudar no crescimento da empresa.
  - Aceleradoras:
  Organizações que ajudam startups a se prepararem para investidores, oferecendo suporte em modelo de negócios, pitch, valuation, entre outros.
  Financiamento Público Não Reembolsável:
  Subvenções públicas que financiam startups inovadoras sem a necessidade de reembolso, como programas da FINEP e FAPESP.
  - Venture Capital:
  Fundos privados que compram participações minoritárias em startups com potencial de crescimento. Geralmente, esse tipo de financiamento é voltado para startups em estágio avançado.
  '''

    full_text = (
        f'Com base no contexto informado e nas informações da empresa, responda a pergunta: "{msg}"\n'
        f'<CONTEXTO>: {context}\n'
        f'<INFORMAÇÕES DA EMPRESA>: {data}'
    )
    return full_text
