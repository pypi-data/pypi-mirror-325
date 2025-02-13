import { i as ae, a as W, r as ue, g as de, w as O, b as fe } from "./Index-4MbJaJER.js";
const y = window.ms_globals.React, oe = window.ms_globals.React.forwardRef, se = window.ms_globals.React.useRef, ie = window.ms_globals.React.useState, le = window.ms_globals.React.useEffect, ce = window.ms_globals.React.useMemo, M = window.ms_globals.ReactDOM.createPortal, me = window.ms_globals.internalContext.useContextPropsContext, U = window.ms_globals.internalContext.ContextPropsProvider, _e = window.ms_globals.antd.List;
var he = /\s/;
function pe(e) {
  for (var t = e.length; t-- && he.test(e.charAt(t)); )
    ;
  return t;
}
var ge = /^\s+/;
function we(e) {
  return e && e.slice(0, pe(e) + 1).replace(ge, "");
}
var z = NaN, be = /^[-+]0x[0-9a-f]+$/i, ye = /^0b[01]+$/i, xe = /^0o[0-7]+$/i, Ee = parseInt;
function B(e) {
  if (typeof e == "number")
    return e;
  if (ae(e))
    return z;
  if (W(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = W(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = we(e);
  var o = ye.test(e);
  return o || xe.test(e) ? Ee(e.slice(2), o ? 2 : 8) : be.test(e) ? z : +e;
}
var j = function() {
  return ue.Date.now();
}, Ce = "Expected a function", ve = Math.max, Ie = Math.min;
function Se(e, t, o) {
  var s, i, n, r, l, u, _ = 0, g = !1, c = !1, w = !0;
  if (typeof e != "function")
    throw new TypeError(Ce);
  t = B(t) || 0, W(o) && (g = !!o.leading, c = "maxWait" in o, n = c ? ve(B(o.maxWait) || 0, t) : n, w = "trailing" in o ? !!o.trailing : w);
  function m(d) {
    var b = s, R = i;
    return s = i = void 0, _ = d, r = e.apply(R, b), r;
  }
  function E(d) {
    return _ = d, l = setTimeout(p, t), g ? m(d) : r;
  }
  function f(d) {
    var b = d - u, R = d - _, D = t - b;
    return c ? Ie(D, n - R) : D;
  }
  function h(d) {
    var b = d - u, R = d - _;
    return u === void 0 || b >= t || b < 0 || c && R >= n;
  }
  function p() {
    var d = j();
    if (h(d))
      return C(d);
    l = setTimeout(p, f(d));
  }
  function C(d) {
    return l = void 0, w && s ? m(d) : (s = i = void 0, r);
  }
  function v() {
    l !== void 0 && clearTimeout(l), _ = 0, s = u = i = l = void 0;
  }
  function a() {
    return l === void 0 ? r : C(j());
  }
  function I() {
    var d = j(), b = h(d);
    if (s = arguments, i = this, u = d, b) {
      if (l === void 0)
        return E(u);
      if (c)
        return clearTimeout(l), l = setTimeout(p, t), m(u);
    }
    return l === void 0 && (l = setTimeout(p, t)), r;
  }
  return I.cancel = v, I.flush = a, I;
}
var Z = {
  exports: {}
}, L = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Re = y, Oe = Symbol.for("react.element"), Te = Symbol.for("react.fragment"), ke = Object.prototype.hasOwnProperty, Pe = Re.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Le = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function $(e, t, o) {
  var s, i = {}, n = null, r = null;
  o !== void 0 && (n = "" + o), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (r = t.ref);
  for (s in t) ke.call(t, s) && !Le.hasOwnProperty(s) && (i[s] = t[s]);
  if (e && e.defaultProps) for (s in t = e.defaultProps, t) i[s] === void 0 && (i[s] = t[s]);
  return {
    $$typeof: Oe,
    type: e,
    key: n,
    ref: r,
    props: i,
    _owner: Pe.current
  };
}
L.Fragment = Te;
L.jsx = $;
L.jsxs = $;
Z.exports = L;
var x = Z.exports;
const {
  SvelteComponent: je,
  assign: G,
  binding_callbacks: H,
  check_outros: Ne,
  children: ee,
  claim_element: te,
  claim_space: Me,
  component_subscribe: K,
  compute_slots: We,
  create_slot: Ae,
  detach: S,
  element: ne,
  empty: q,
  exclude_internal_props: V,
  get_all_dirty_from_scope: Fe,
  get_slot_changes: De,
  group_outros: Ue,
  init: ze,
  insert_hydration: T,
  safe_not_equal: Be,
  set_custom_element_data: re,
  space: Ge,
  transition_in: k,
  transition_out: A,
  update_slot_base: He
} = window.__gradio__svelte__internal, {
  beforeUpdate: Ke,
  getContext: qe,
  onDestroy: Ve,
  setContext: Je
} = window.__gradio__svelte__internal;
function J(e) {
  let t, o;
  const s = (
    /*#slots*/
    e[7].default
  ), i = Ae(
    s,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = ne("svelte-slot"), i && i.c(), this.h();
    },
    l(n) {
      t = te(n, "SVELTE-SLOT", {
        class: !0
      });
      var r = ee(t);
      i && i.l(r), r.forEach(S), this.h();
    },
    h() {
      re(t, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      T(n, t, r), i && i.m(t, null), e[9](t), o = !0;
    },
    p(n, r) {
      i && i.p && (!o || r & /*$$scope*/
      64) && He(
        i,
        s,
        n,
        /*$$scope*/
        n[6],
        o ? De(
          s,
          /*$$scope*/
          n[6],
          r,
          null
        ) : Fe(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      o || (k(i, n), o = !0);
    },
    o(n) {
      A(i, n), o = !1;
    },
    d(n) {
      n && S(t), i && i.d(n), e[9](null);
    }
  };
}
function Xe(e) {
  let t, o, s, i, n = (
    /*$$slots*/
    e[4].default && J(e)
  );
  return {
    c() {
      t = ne("react-portal-target"), o = Ge(), n && n.c(), s = q(), this.h();
    },
    l(r) {
      t = te(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), ee(t).forEach(S), o = Me(r), n && n.l(r), s = q(), this.h();
    },
    h() {
      re(t, "class", "svelte-1rt0kpf");
    },
    m(r, l) {
      T(r, t, l), e[8](t), T(r, o, l), n && n.m(r, l), T(r, s, l), i = !0;
    },
    p(r, [l]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, l), l & /*$$slots*/
      16 && k(n, 1)) : (n = J(r), n.c(), k(n, 1), n.m(s.parentNode, s)) : n && (Ue(), A(n, 1, 1, () => {
        n = null;
      }), Ne());
    },
    i(r) {
      i || (k(n), i = !0);
    },
    o(r) {
      A(n), i = !1;
    },
    d(r) {
      r && (S(t), S(o), S(s)), e[8](null), n && n.d(r);
    }
  };
}
function X(e) {
  const {
    svelteInit: t,
    ...o
  } = e;
  return o;
}
function Ye(e, t, o) {
  let s, i, {
    $$slots: n = {},
    $$scope: r
  } = t;
  const l = We(n);
  let {
    svelteInit: u
  } = t;
  const _ = O(X(t)), g = O();
  K(e, g, (a) => o(0, s = a));
  const c = O();
  K(e, c, (a) => o(1, i = a));
  const w = [], m = qe("$$ms-gr-react-wrapper"), {
    slotKey: E,
    slotIndex: f,
    subSlotIndex: h
  } = de() || {}, p = u({
    parent: m,
    props: _,
    target: g,
    slot: c,
    slotKey: E,
    slotIndex: f,
    subSlotIndex: h,
    onDestroy(a) {
      w.push(a);
    }
  });
  Je("$$ms-gr-react-wrapper", p), Ke(() => {
    _.set(X(t));
  }), Ve(() => {
    w.forEach((a) => a());
  });
  function C(a) {
    H[a ? "unshift" : "push"](() => {
      s = a, g.set(s);
    });
  }
  function v(a) {
    H[a ? "unshift" : "push"](() => {
      i = a, c.set(i);
    });
  }
  return e.$$set = (a) => {
    o(17, t = G(G({}, t), V(a))), "svelteInit" in a && o(5, u = a.svelteInit), "$$scope" in a && o(6, r = a.$$scope);
  }, t = V(t), [s, i, g, c, l, u, r, n, C, v];
}
class Qe extends je {
  constructor(t) {
    super(), ze(this, t, Ye, Xe, Be, {
      svelteInit: 5
    });
  }
}
const Y = window.ms_globals.rerender, N = window.ms_globals.tree;
function Ze(e, t = {}) {
  function o(s) {
    const i = O(), n = new Qe({
      ...s,
      props: {
        svelteInit(r) {
          window.ms_globals.autokey += 1;
          const l = {
            key: window.ms_globals.autokey,
            svelteInstance: i,
            reactComponent: e,
            props: r.props,
            slot: r.slot,
            target: r.target,
            slotIndex: r.slotIndex,
            subSlotIndex: r.subSlotIndex,
            ignore: t.ignore,
            slotKey: r.slotKey,
            nodes: []
          }, u = r.parent ?? N;
          return u.nodes = [...u.nodes, l], Y({
            createPortal: M,
            node: N
          }), r.onDestroy(() => {
            u.nodes = u.nodes.filter((_) => _.svelteInstance !== i), Y({
              createPortal: M,
              node: N
            });
          }), l;
        },
        ...s.props
      }
    });
    return i.set(n), n;
  }
  return new Promise((s) => {
    window.ms_globals.initializePromise.then(() => {
      s(o);
    });
  });
}
const $e = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function et(e) {
  return e ? Object.keys(e).reduce((t, o) => {
    const s = e[o];
    return t[o] = tt(o, s), t;
  }, {}) : {};
}
function tt(e, t) {
  return typeof t == "number" && !$e.includes(e) ? t + "px" : t;
}
function F(e) {
  const t = [], o = e.cloneNode(!1);
  if (e._reactElement) {
    const i = y.Children.toArray(e._reactElement.props.children).map((n) => {
      if (y.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: l
        } = F(n.props.el);
        return y.cloneElement(n, {
          ...n.props,
          el: l,
          children: [...y.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return i.originalChildren = e._reactElement.props.children, t.push(M(y.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: i
    }), o)), {
      clonedElement: o,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((i) => {
    e.getEventListeners(i).forEach(({
      listener: r,
      type: l,
      useCapture: u
    }) => {
      o.addEventListener(l, r, u);
    });
  });
  const s = Array.from(e.childNodes);
  for (let i = 0; i < s.length; i++) {
    const n = s[i];
    if (n.nodeType === 1) {
      const {
        clonedElement: r,
        portals: l
      } = F(n);
      t.push(...l), o.appendChild(r);
    } else n.nodeType === 3 && o.appendChild(n.cloneNode());
  }
  return {
    clonedElement: o,
    portals: t
  };
}
function nt(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const P = oe(({
  slot: e,
  clone: t,
  className: o,
  style: s,
  observeAttributes: i
}, n) => {
  const r = se(), [l, u] = ie([]), {
    forceClone: _
  } = me(), g = _ ? !0 : t;
  return le(() => {
    var E;
    if (!r.current || !e)
      return;
    let c = e;
    function w() {
      let f = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (f = c.children[0], f.tagName.toLowerCase() === "react-portal-target" && f.children[0] && (f = f.children[0])), nt(n, f), o && f.classList.add(...o.split(" ")), s) {
        const h = et(s);
        Object.keys(h).forEach((p) => {
          f.style[p] = h[p];
        });
      }
    }
    let m = null;
    if (g && window.MutationObserver) {
      let f = function() {
        var v, a, I;
        (v = r.current) != null && v.contains(c) && ((a = r.current) == null || a.removeChild(c));
        const {
          portals: p,
          clonedElement: C
        } = F(e);
        c = C, u(p), c.style.display = "contents", w(), (I = r.current) == null || I.appendChild(c);
      };
      f();
      const h = Se(() => {
        f(), m == null || m.disconnect(), m == null || m.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: i
        });
      }, 50);
      m = new window.MutationObserver(h), m.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", w(), (E = r.current) == null || E.appendChild(c);
    return () => {
      var f, h;
      c.style.display = "", (f = r.current) != null && f.contains(c) && ((h = r.current) == null || h.removeChild(c)), m == null || m.disconnect();
    };
  }, [e, g, o, s, n, i]), y.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...l);
});
function rt(e) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(e.trim());
}
function ot(e, t = !1) {
  try {
    if (fe(e))
      return e;
    if (t && !rt(e))
      return;
    if (typeof e == "string") {
      let o = e.trim();
      return o.startsWith(";") && (o = o.slice(1)), o.endsWith(";") && (o = o.slice(0, -1)), new Function(`return (...args) => (${o})(...args)`)();
    }
    return;
  } catch {
    return;
  }
}
function st(e, t) {
  return ce(() => ot(e, t), [e, t]);
}
function Q(e, t) {
  return e ? /* @__PURE__ */ x.jsx(P, {
    slot: e,
    clone: t == null ? void 0 : t.clone
  }) : null;
}
function it({
  key: e,
  slots: t,
  targets: o
}, s) {
  return t[e] ? (...i) => o ? o.map((n, r) => /* @__PURE__ */ x.jsx(U, {
    params: i,
    forceClone: (s == null ? void 0 : s.forceClone) ?? !0,
    children: Q(n, {
      clone: !0,
      ...s
    })
  }, r)) : /* @__PURE__ */ x.jsx(U, {
    params: i,
    forceClone: (s == null ? void 0 : s.forceClone) ?? !0,
    children: Q(t[e], {
      clone: !0,
      ...s
    })
  }) : void 0;
}
const ct = Ze(({
  slots: e,
  renderItem: t,
  setSlotParams: o,
  ...s
}) => {
  const i = st(t);
  return /* @__PURE__ */ x.jsx(_e, {
    ...s,
    footer: e.footer ? /* @__PURE__ */ x.jsx(P, {
      slot: e.footer
    }) : s.footer,
    header: e.header ? /* @__PURE__ */ x.jsx(P, {
      slot: e.header
    }) : s.header,
    loadMore: e.loadMore ? /* @__PURE__ */ x.jsx(P, {
      slot: e.loadMore
    }) : s.loadMore,
    renderItem: e.renderItem ? it({
      slots: e,
      setSlotParams: o,
      key: "renderItem"
    }, {
      forceClone: !0
    }) : i
  });
});
export {
  ct as List,
  ct as default
};
